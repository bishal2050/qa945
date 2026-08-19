import time

from locators.Locator import locate

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login:
    def __init__(self,driver):
        self.browser = driver
        self.lc = locate()

    def get_nav_id(self):
        return self.browser.find_element(By.ID, self.lc.login_nav_bar_id)

    def click_nav_id(self):
        self.get_nav_id().click()

    def get_username(self):
        return WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.ID, self.lc.login_username_id)))

    def send_username(self,username):
        self.get_username().send_keys(username)

    def get_password(self):
        return self.browser.find_element(By.ID, self.lc.login_password_id)

    def send_password(self,password):
        self.get_password().send_keys(password)

    def get_login_button(self):
        return self.browser.find_element(By.XPATH, self.lc.login_button_xpath)

    def click_login_button(self):
        self.get_login_button().click()


    def loginpage(self,usname,pwd):
        self.click_nav_id()
        self.send_username(usname)
        self.send_password(pwd)
        self.click_login_button()
        time.sleep(10)