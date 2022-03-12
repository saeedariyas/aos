import sys
from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

import aos_locators as locators
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

s = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=s)
a = ActionChains(driver)


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
    if driver.current_url == locators.app_url:
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


def checkhomepagetextsandlinks():
    if driver.current_url == locators.app_url:
        for i in range(len(locators.list_txtid)):
            sleep(0.25)
            ids, lbls, txts = locators.list_txtid[i], locators.list_lblid[i], locators.list_txt[i]
            print(ids, lbls, txts)
            assert driver.find_element(By.ID, ids).is_displayed()
            m = driver.find_element(By.ID, ids)
            a.move_to_element(m).perform()
            driver.find_element(By.ID, lbls).click()
            assert driver.find_element(By.LINK_TEXT, txts).is_displayed()
            print(f'{txts} - SHOP NOW clickable')
            driver.find_element(By.LINK_TEXT, 'HOME').click()

        '''assert driver.find_element(By.ID, 'speakersTxt').is_displayed()
        # object of ActionChains
        a = ActionChains(driver)
        # identify element
        m = driver.find_element(By.ID, 'speakersTxt')
        # hover over element
        a.move_to_element(m).perform()
        #driver.find_element(By.ID, 'speakersImg')
        driver.find_element(By.ID, 'speakersLink').click()'''


def checktopnav():
    if driver.current_url == locators.app_url:
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()

        assert driver.find_element(By.XPATH, '//h3[contains(.,"SPECIAL OFFER")]').is_displayed()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
        assert driver.find_element(By.XPATH, '//h3[contains(.,"POPULAR ITEMS")]').is_displayed()
        sleep(2)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        assert driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
        print('topmenu checking success')


def checklogo():
    if driver.current_url == locators.app_url:
        sleep(2)
        assert driver.find_element(By.ID, 'Layer_1').is_displayed()
        assert driver.find_element(By.XPATH, '//span[contains(.,"dvantage")]').is_displayed()
        assert driver.find_element(By.XPATH, '//span[contains(.,"DEMO")]').is_displayed()
        print('logo displayed')

def checkcontactform():
    if driver.current_url == locators.app_url:
        sleep(3)
        driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
        sleep(0.2)
        assert driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
        Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text("Laptops")
        sleep(0.25)
        Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text("HP Chromebook 14 G1(ENERGY STAR)")
        sleep(0.25)
        driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email1)
        sleep(0.25)
        driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)

        driver.find_element(By.ID,'send_btnundefined').click()
        sleep(0.25)
        assert driver.find_element(By.XPATH, '//p[text()="Thank you for contacting Advantage support."]').is_displayed()
        #assert driver.find_element(By.XPATH, '//p[contains(.," Thank you for contacting Advantage support. ")]').is_displayed()
        print("value selected")
        sleep(2)
        #driver.find_element(By.LINK_TEXT,' CONTINUE SHOPPING ').click()
        driver.find_element(By.XPATH, '//a[contains(.,"CONTINUE SHOPPING")]').click()
        sleep(0.25)
        print('contact us form checked')

def checksocialmedialinks():
    if driver.current_url == locators.app_url:
        sleep(3)
        driver.find_element(By.NAME,'follow_facebook').click()
        driver.find_element(By.NAME, 'follow_twitter').click()
        driver.find_element(By.NAME, 'follow_linkedin').click()
        print('social media links worked')


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
checkhomepagetextsandlinks()
checktopnav()
checklogo()
checkcontactform()
checksocialmedialinks()
tearDown()'''
