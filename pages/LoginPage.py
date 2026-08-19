import logging

from selenium.webdriver.common.by import By

from locators.Locate import Locator
class Login:
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s')
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locator()

    def get_nav_login(self):
        return self.driver.find_element(By.LINK_TEXT, self.lc.login_nav)

    def click_login_nav(self):
        self.get_nav_login().click()

    def get_username_field(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element(By.ID, self.lc.txt_uname_id)

    def enter_uname(self, username):
        self.get_username_field().send_keys(username)

    def get_password_field(self):
        return self.driver.find_element(By.ID, self.lc.txt_pswd_id)

    def enter_password(self, password):
        self.get_password_field().send_keys(password)

    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.lc.btn_login_xpath)

    def click_login_button(self):
        self.get_login_button().click()

    def login(self, username, password):
        txt = self.get_nav_login().text
        logging.log(logging.INFO, f"Clicking login navigation link. {txt}")
        self.click_login_nav()
        self.enter_uname(username)
        self.enter_password(password)
        self.click_login_button()

