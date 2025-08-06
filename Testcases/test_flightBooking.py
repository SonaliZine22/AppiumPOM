from datetime import time
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import scroll_util


def test_flightBooking(appium_driver):
    driver = appium_driver
    driver.get("https://www.makemytrip.com/")
    wait = WebDriverWait(driver, 30)
    close_button = wait.until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//span[@data-cy='loginBottomsheetCrossClick']")))
    close_button.click()
    driver.find_element(AppiumBy.XPATH, "//a[@data-cy='menu_item_clicked_0']").click()
    driver.find_element(AppiumBy.XPATH, "//li[@data-cy='tab ROUNDTRIP']").click()
    driver.find_element(AppiumBy.XPATH,"//div[@data-cy='fromCity']").click()
    driver.find_element(AppiumBy.XPATH, "//input[@data-cy='select-from-input']").send_keys("Mumbai")
    try:
        element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((AppiumBy.XPATH, "(//div[@class='makeFlex flexOne'])[1]"))
        )git
        element.click()
    except StaleElementReferenceException:
        print("StaleElementReferenceException occurred.")
    driver.implicitly_wait(5)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.XPATH, "//div[@data-cy='toCity']"))
    ).click()
    #driver.find_element(AppiumBy.XPATH,"//div[@data-cy='toCity']").click()
    driver.implicitly_wait(5)
    driver.find_element(AppiumBy.XPATH, "//input[@data-cy='select-to-input']").send_keys("thailand")
    try:

        driver.find_element(AppiumBy.XPATH, "(//div[@class='makeFlex column flexOne'])[5]").click()
    except StaleElementReferenceException:
        print("StaleElementReferenceException occurred.")
    driver.find_element(AppiumBy.XPATH, "//div[@data-cy='departure']").click()
    driver.find_element(AppiumBy.XPATH, "//div[@data-cy='fromCalendar']").click()
    driver.find_element(AppiumBy.XPATH,"//div[@aria-label='Mon Aug 25 2025']").click()
    driver.find_element(AppiumBy.XPATH, "//div[@data-cy='toCalendar']").click()
    driver.find_element(AppiumBy.XPATH, "//div[@aria-label='Sat Aug 30 2025']").click()
    driver.find_element(AppiumBy.XPATH, "//a[@data-cy='calendarDone']").click()
    driver.find_element(AppiumBy.XPATH,"//div[@data-cy='traveller']").click()
    driver.find_element(AppiumBy.XPATH, "//span[@data-cy='Adults-increment']").click()
    driver.find_element(AppiumBy.XPATH, "//span[@data-cy='Adults-increment']").click()
    driver.find_element(AppiumBy.XPATH, "//span[@data-cy='Adults-increment']").click()
    driver.find_element(AppiumBy.XPATH, "//span[@data-cy='Infants-increment']").click()
    driver.find_element(AppiumBy.XPATH, "//span[@data-cy='Infants-increment']").click()
    driver.find_element(AppiumBy.XPATH,"//button[@data-cy='travelSubmit']").click()
    driver.find_element(AppiumBy.XPATH,"//button[@data-cy='search']").click()
    print("Flight Search Successfully")







