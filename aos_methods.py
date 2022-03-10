import sys
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service

import aos_locators as locators
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print('--------------------~*~--------------------')
    # Make browser full screen
    driver.maximize_window()
    # Give browser up to 30 seconds to respond
    driver.implicitly_wait(30)
    # Navigate to Advantage  website
    driver.get(locators.app_url)
    print(driver.current_url)
    print(driver.title)

    if driver.current_url == locators.app_url and driver.title == locators.home_page_title:
        print(f'Yey! {locators.app} Launched Successfully')
        print(f'{locators.app} homepage URL: {driver.current_url}\nHome Page Title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app}  did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page Title: {driver.title}')
        tearDown()


def createnewuser():
    print('........Creating new account.......')

    driver.find_element(By.ID, 'menuUserSVGPath').click()
    sleep(3)

    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()

    assert driver.find_element(By.LINK_TEXT, 'CREATE ACCOUNT').is_displayed()
    print('........Create new account page is displayed.......')
    # driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(first_name)
    driver.find_element(By.NAME, 'addressRegisterPage').clear()
    for i in range(len(locators.list_names)):
        name, val = locators.list_names[i], locators.list_val[i]
        driver.find_element(By.NAME, name).send_keys(val)
        sleep(0.25)

        # To select country from drop down

        # Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(country)
    sleep(0.25)

    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)
    print("Registration complete")

    # assert driver.find_element(By.XPATH, f'//span[contains(.,{new_username})]').is_displayed()
    assert driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed()
    print('........ Validated - New Account created........ ')


def log_in():
    if driver.current_url == 'https://advantageonlineshopping.com/#/':
        print('Sign in page displayed')
        sleep(3)
        # driver.find_element(By.ID, 'menuUserSVGPath').click()
        driver.find_element(By.ID, 'menuUserLink').click()
        # driver.find_element(By.ID, 'menuUser').click()
        print('........New user Signing in......')
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.25)
        assert driver.find_element(By.LINK_TEXT, locators.new_username).is_displayed()
        # print('Signed in')
        print('........ Validated - Signed in successfully........ ')
        sleep(3)


def log_out():
    # Logout
    driver.find_element(By.ID, 'menuUser').click()
    # breakpoint()

    # driver.find_element(By.LINK_TEXT,'Sign out').click()
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(.,"Sign out")]').click()
    print("User logged out")


def tearDown():
    if driver is not None:
        print('--------------------~*~--------------------')
        print(f'The test Completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


'''setUp()
createnewuser()
log_out()
log_in()
log_out()
tearDown()'''
