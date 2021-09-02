import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class ArgyleChallenge(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://selenium:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

    def test_login_invalid_credentials(self):
        driver = self.driver
        wait = WebDriverWait(self.driver, 10)
        driver.get('https://console.argyle.com/')

        emailField = driver.find_element_by_id('sign-in-email')
        emailField.clear()
        emailField.send_keys("test@test.com")

        passwordField = driver.find_element_by_id('sign-in-passowrd')
        passwordField.clear()
        passwordField.send_keys("Password123!@#")

        btnSignIn = driver.find_element_by_class_name('Button__ButtonContent-sc-193vxdm-5')
        btnSignIn.click()

        wait.until(EC.element_to_be_clickable((By.ID, 'sign-in-email-helper')))
        txtInvalidCredentialsMsg = driver.find_element_by_id('sign-in-email-helper').text
        self.assertEqual(txtInvalidCredentialsMsg, 'Invalid email and password combination', 'Login Error message is not correct.')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()