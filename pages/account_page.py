from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.deposit_button = ("xpath", "//button[contains(text(), 'Deposit')]")
        self.withdrawl_button = ("xpath", "//button[contains(text(), 'Withdrawl')]")
        self.transactions_button = ("xpath", "//button[contains(text(), 'Transactions')]")
        self.balance_text = ("xpath", "//div[@class='center' and contains(text(), 'Balance')]//strong[1]")
        self.deposit_amount_input = ("xpath", "//input[@placeholder='amount']")
        self.submit_deposit_button = ("xpath", "//button[@type='submit' and contains(text(), 'Deposit')]")


    def get_balance(self):
        balance = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.balance_text)
        )
        return int(balance.text)


    def deposit(self, amount):
        self.driver.find_element(*self.deposit_button).click()
        amount_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.deposit_amount_input)
        )
        amount_input.clear()
        amount_input.send_keys(str(amount))
        self.driver.find_element(*self.submit_deposit_button).click()


    def withdraw(self, amount):
        self.driver.find_element(*self.withdrawl_button).click()
        amount_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.deposit_amount_input)
        )
        amount_input.clear()
        amount_input.send_keys(str(amount))
        self.driver.find_element(*self.submit_deposit_button).click()


    def open_transactions(self):
        self.driver.find_element(*self.transactions_button).click()