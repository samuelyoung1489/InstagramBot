from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')

        login_link = browser.find_element_by_xpath("//a[text()='Log in']")
        login_link.click()

        emailInput = self.browser.find_element_by_Class_name('_2hvTZ pexuQ zyHYP')
        passwordInput = self.browser.find_element_by_Class_name('_2hvTZ pexuQ zyHYP')

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        username_input = browser.find_element_by_css_selector("input[name='username']")
        password_input = browser.find_element_by_css_selector("input[name='password']")

        username_input.send_keys("<your username>")
        password_input.send_keys("<your password>")
        time.sleep(2)


bot = InstagramBot('samsam978@hvc.rr.com', 'Password')
bot.signIn()
