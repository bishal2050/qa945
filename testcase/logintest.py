import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import Login
from locators.Locate import Locator

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")
        self.lp = Login(self.driver)
        self.lc = Locator()

    def test_a_login(self):
        self.lp.login("testmorning", "test123")
        ww = WebDriverWait(self.driver, 10)
        ww.until(EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome testmorning"))
        name = self.driver.find_element(By.ID,self.lc.lbl_welcome_id).text
        self.assertEqual(name, "Welcome testmorning", "Login failed or username not displayed correctly.")


    def test_b_login_invalid(self):
        self.lp.login("testmorning", "invalidpass")
        # Assuming the application shows an alert for invalid login
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        Alert = self.driver.switch_to.alert
        self.assertEqual(Alert.text, "Wrong password.", "Alert message not displayed correctly.")
        Alert.accept()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
