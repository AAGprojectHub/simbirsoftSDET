from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_login_button = ("xpath", "/html/body/div/div/div[2]/div/div[1]/div[1]/button")


    def open(self, url):
        self.driver.get(url)


    def click_customer_login(self):
        self.driver.find_element(*self.customer_login_button).click()