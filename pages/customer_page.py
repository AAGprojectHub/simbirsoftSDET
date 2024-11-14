from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomerPage:
    def __init__(self, driver):
        self.driver = driver
        self.customer_select = ("xpath", '//*[@id="userSelect"]')
        self.login_button = ("xpath", "button[type='submit']")


    def open(self, url):
        self.driver.get(url)


    def select_customer(self, customer_name):
        select_element = self.driver.find_element(*self.customer_select)
        select_element.click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(("xpath", f"//option[text()='{customer_name}']"))
        )
        select = Select(select_element)
        select.select_by_visible_text(customer_name)


    def click_login(self):
        self.driver.find_element(*self.login_button).click()