from datetime import time
from selenium.common.exceptions import NoSuchElementException
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities import scroll_util


def test_login(appium_driver):
    driver = appium_driver
    driver.get("https://www.makemytrip.com/")
    wait = WebDriverWait(driver, 30)
    close_button = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//span[@data-cy='loginBottomsheetCrossClick']")))
    close_button.click()
    driver.find_element(AppiumBy.XPATH, "//a[@data-cy='menu_item_clicked_1']").click()
    driver.implicitly_wait(20)
    driver.find_element(AppiumBy.XPATH,"//span[@class='mdWidgetFld__label']").click()
    driver.find_element(AppiumBy.XPATH, "//input[@data-cy='select-location-input']").send_keys("pune")
    driver.find_element(AppiumBy.XPATH, "(//p[@class='srchSublist__item--title '])[5]").click()
    driver.find_element(AppiumBy.XPATH,"(//div[@class='mdWidgetFld  tapEffect   '])[2]").click()
    driver.find_element(AppiumBy.XPATH, "//div[@aria-label='Fri Aug 22 2025']").click()
    driver.find_element(AppiumBy.XPATH, "//div[@data-cy='cal-checkout']").click()
    driver.find_element(AppiumBy.XPATH, "//div[@aria-label='Sat Aug 30 2025']").click()
    driver.find_element(AppiumBy.XPATH,"//a[@data-cy='cal-done']").click()
    driver.find_element(AppiumBy.XPATH,"(//span[@class='counterWrap__value'])[1]").click()
    driver.find_element(AppiumBy.XPATH,"//ul[@data-cy='HotelGuests_RoomsDropdown']//li[@data-cy='HotelGuests_RoomsDropdownItem2']").click()
    driver.find_element(AppiumBy.XPATH, "(//span[@class='counterWrap__value'])[2]").click()
    driver.find_element(AppiumBy.XPATH, "//ul[@data-cy='HomestayGuests_AdultsDropdown']//li[@data-cy='HomestayGuests_AdultsDropdownItem3']").click()
    driver.find_element(AppiumBy.XPATH, "(//span[@class='counterWrap__value'])[3]").click()
    driver.find_element(AppiumBy.XPATH,
                        "//ul[@data-cy='HomestayGuests_ChildrenDropdown']//li[@data-cy='HomestayGuests_ChildrenDropdownItem2']").click()

    driver.find_element(AppiumBy.XPATH, "(//span[@class='counterWrap__value'])[4]").click()
    driver.find_element(AppiumBy.XPATH,
                        "//ul[@data-cy='HomestayGuests_Child1Dropdown']//li[@data-cy='HomestayGuests_Child1DropdownItem0']").click()
    driver.find_element(AppiumBy.XPATH, "(//span[@class='counterWrap__value'])[5]").click()
    driver.find_element(AppiumBy.XPATH,
                        "//ul[@data-cy='HomestayGuests_Child2Dropdown']//li[@data-cy='HomestayGuests_Child2DropdownItem1']").click()

    driver.find_element(AppiumBy.XPATH,"//button[@class='font16 lato-black button primaryBtn']").click()
    driver.find_element(AppiumBy.XPATH,"//button[@data-cy='HotelWidgetForm_127']").click()
    driver.implicitly_wait(10)

    try:
        driver.find_element(AppiumBy.XPATH, "//a[@data-testid='btmSheet-closeBtn']").click()
        print("Close button clicked successfully.")
    except NoSuchElementException:
        print("Close button not found.")
    driver.implicitly_wait(10)

    # hotel =driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
    #     'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Hotel Vrindavan"))'
    # )



    for i in range(3):
        try:
            hotel = driver.find_element(AppiumBy.XPATH, "(//div[@class='flexOne makeFlex'])[4]")
            driver.execute_script("arguments[0].scrollIntoView(true);", hotel)
            hotel.click()
            print("Hotel clicked.")
            break
        except NoSuchElementException:
            driver.execute_script("window.scrollBy(0, 500);")
            driver.implicitly_wait(10)

    driver.implicitly_wait(10)





