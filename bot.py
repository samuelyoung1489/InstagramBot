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

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]

        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)

        notNow = self.browser.find_elements_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]')
        notNow.send_keys(Keys.ENTER)

        time.sleep(2)


bot = InstagramBot('samsam978@hvc.rr.com', 'Password')
bot.signIn()
