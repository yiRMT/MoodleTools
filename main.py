# Library imports
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os
from dotenv import load_dotenv
from one_time_password import otp
from time import sleep


def open_login_page(browser):
    login_cls = browser.find_element_by_class_name("login")
    login_btn = login_cls.find_element_by_tag_name("a")
    login_btn.click()


def login(browser):
    # ログイン情報入力
    username = browser.find_element_by_name("SM_UID")
    text_username = os.getenv("OMUID")
    username.send_keys(text_username)

    password = browser.find_element_by_name("SM_PWD")
    text_password = os.getenv("PASSWORD")
    password.send_keys(text_password)

    username.submit()


def two_factor_authentication(browser):
    onetime_password = browser.find_element_by_name("SM_PWD")
    text_onetime_password = otp()
    onetime_password.send_keys(text_onetime_password)
    onetime_password.submit()


def main():
    # Import .env file
    load_dotenv()

    # Browser instance
    browser = webdriver.Chrome(ChromeDriverManager().install())

    # Open Moodle
    moodle_url = "https://lms.omu.ac.jp"
    browser.get(moodle_url)

    # Open login page
    open_login_page(browser)

    # Login
    if browser.current_url == "https://auth.omu.ac.jp/AuthServer/AuthRequest":
        login(browser)

    # Two factor authentication
    if browser.current_url == ('https://auth.omu.ac.jp/AuthServer/SMAuthenticator'):
        two_factor_authentication(browser)

    sleep(2)


if __name__ == "__main__":
    main()
