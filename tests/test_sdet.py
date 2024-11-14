import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from pages.login_page import LoginPage
from pages.customer_page import CustomerPage
from pages.account_page import AccountPage
from pages.transaction_page import TransactionPage
from utils.fibonacci import fibonacci


@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=options,
        desired_capabilities={'browserName': 'chrome'}
    )
    yield driver
    driver.quit()


def test_banking_operations(driver):
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    customer_name = "Harry Potter"
    n = datetime.now().day + 1
    fib_number = fibonacci(n)

    # Шаг 1: Авторизация 1/2
    login_page = LoginPage(driver)
    login_page.open(url)
    login_page.click_customer_login()

    # Шаг 2: Авторизация 2/2
    customer_page = CustomerPage(driver)
    customer_page.select_customer(customer_name)
    customer_page.click_login()

    # Шаг 3: Депозит и снятие
    account_page = AccountPage(driver)
    account_page.deposit(fib_number)
    account_page.withdraw(fib_number)

    # Шаг 4: Проверка баланса
    balance = account_page.get_balance()
    assert balance == 0, "Баланс не равен нулю!"

    # Шаг 5: Проверка и сохранение транзакций
    account_page.go_to_transactions()
    transaction_page = TransactionPage(driver)
    transactions = transaction_page.get_transactions()
    assert len(transactions) >= 2, "Не удалось найти обе транзакции!"

    # Шаг 5: Сохранение транзакций в CSV
    csv_file = "/tmp/transactions.csv"
    transaction_page.save_transactions_to_csv(transactions, csv_file)

    # Шаг 6: Прикрепление CSV-файла к отчету Allure
    with open(csv_file, "rb") as f:
        allure.attach(f.read(), name="Transactions", attachment_type=allure.attachment_type.CSV)