import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.scroll_util import ScrollUtil


# from Pages.HomeScreen import HomeScreen
# from Pages.HotelScreen import HotelScreen
# from TestCases.BaseTest import BaseTest
# from Utilities import dataProvider
# from Utilities.scroll_util import ScrollUtil




#@pytest.mark.parametrize("city,hotel", dataProvider.get_data("VillaTest"))
def test_login(appium_driver):
    driver = appium_driver
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(AppiumBy.XPATH, "//input[@name='username']").send_keys("Admin")
    driver.find_element(AppiumBy.XPATH, "//input[@name='password']").send_keys("admin123")
    driver.find_element(AppiumBy.XPATH, "//button[@type='submit']").click()
    driver.implicitly_wait(10)
    #driver.find_element(AppiumBy.XPATH, "// button[contains(text(), 'Login')]").click()

    # element = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((AppiumBy.XPATH, "//span[text()='Assign Leave']"))
    # )
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # element.click()

# driver.implicitly_wait(10)
    # wait = WebDriverWait(driver, 20)
    # element = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//button[@title='Assign Leave']")))
    # driver.execute_script("arguments[0].scrollIntoView(true);", element)
    # driver.execute_script("arguments[0].click();", element)
    # driver.find_element(AppiumBy.XPATH, "//input[@placeholder='Type for hints...']").send_keys("sania shaheen")
    # driver.implicitly_wait(2)
    # driver.find_element(AppiumBy.XPATH, "//input[contains(text(), 'sania shaheen')]").click()
    # driver.find_element(AppiumBy.XPATH,"//div[contains(text(), 'CAN - Vacation')]").click()
    # driver.find_element(AppiumBy.XPATH,"//div//div[1]//div[2]//div[2]//div//div//form//div[3]//div//div[1]//div//div[2]//div//div//i").click()






