import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope="function")
def appium_driver(request):
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("platformVersion", "15")  # ✅ API Level 34 or 33 is better than 36
    options.set_capability("deviceName", "emulator-5554")
    options.set_capability("automationName", "UiAutomator2")

    # 🔧 App-specific capabilities
    options.set_capability("app", r"C:\Users\zine_s\Downloads\com.goibibo_18.1.1.apk")
    options.set_capability("appActivity", ".common.HomeActivity")
    options.set_capability("appWaitActivity", "*")

    # ✅ Extra stability features
    options.set_capability("noReset", True)
    options.set_capability("autoGrantPermissions", True)
    options.set_capability("autoWebview", False)
    options.set_capability("ignoreHiddenApiPolicyError", True)
    options.set_capability("uiautomator2ServerInstallTimeout", 60000)
    options.set_capability("adbExecTimeout", 60000)

    # ✅ Only use chromedriverExecutable if automating WebViews
    # Remove it if you are not doing web automation inside the app yet
    # options.set_capability("chromedriverExecutable", r"C:\path\to\your\chromedriver.exe")

    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)
    request.cls.driver = driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    if request.node.rep_call.failed:
        allure.attach(
            appium_driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=AttachmentType.PNG
        )

# import allure
# import pytest
# from allure_commons.types import AttachmentType
# from appium import webdriver
# from selenium.webdriver.chrome.options import Options
# from appium.options.android import UiAutomator2Options
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     return rep
#
#
# @pytest.fixture(scope="function")
# def appium_driver(request):
#     options = UiAutomator2Options()
#     options.set_capability("platformName", "Android")
#     options = UiAutomator2Options()
#     options.set_capability("platformName", "Android")
#     options.set_capability("platformVersion", "16")  # ✅ Use API 30 or higher
#     options.set_capability("deviceName", "emulator-5554")
#     options.set_capability("automationName", "UiAutomator2")
#     options.set_capability("noReset", True)
#     options.set_capability("appWaitActivity", "*")
#     options.set_capability("autoGrantPermissions", True)
#     options.set_capability("autoWebview", False)
#     options.set_capability("ignoreHiddenApiPolicyError", True)  # ✅ Added
#     options.set_capability("chromedriverExecutable",
#                            "C:\\Users\\zine_s\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
#     options.set_capability("app",
#                            "C:\\Users\\zine_s\\Downloads\\com.goibibo_18.1.1-2068_minAPI26(arm64-v8a,armeabi,armeabi-v7a,x86,x86_64)(nodpi)_apkmirror.com.apk")
#     options.set_capability("appActivity", ".common.HomeActivity")
#
#     driver = webdriver.Remote('http://localhost:4723', options=options)
#     request.cls.driver = driver
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()
#
#
# @pytest.fixture()
# def log_on_failure(request, appium_driver):
#     yield
#     item = request.node
#     driver = appium_driver
#     if item.rep_call.failed:
#         allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
