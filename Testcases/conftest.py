import time

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.hookimpl(hookwrapper=True , tryfirst= True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture(scope="function")
def appium_driver(request):
    # Start Appium Service
    # appium_service = AppiumService()
    # appium_service.start()



    options = Options()
    options.set_capability("platformName", "Android")
    options.set_capability("platformVersion", "16")
    options.set_capability("deviceName", "emulator-5554")
    options.set_capability("browserName","Chrome")
    options.set_capability("automationName", "UiAutomator2")
    options.set_capability("noReset", True)
    #options.set_capability("app", "C:\\Users\\zine_s\\Downloads\\Android.SauceLabs.Mobile.Sample.app.2.7.1.apk")
    options.set_capability("appWaitActivity", "*")
    options.set_capability("autoGrantPermissions", True)
    options.set_capability("autoWebview", False)
    options.set_capability("chromedriverExecutable","C:\\Users\\zine_s\\Downloads\\chromedriver-win64 (2)\\chromedriver-win64\\chromedriver.exe")
    options.set_capability("uiautomator2ServerInstallTimeout", 60000)  # 60 seconds

    # Start driver
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(5)
    yield driver
    time.sleep(2)
    driver.quit()
    # appium_service.stop()

@pytest.fixture()
def log_on_failure(request, appium_driver):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(appium_driver.get_screenshot_as_png(), name="screenshot_on_failure",
                      attachment_type=AttachmentType.PNG)


