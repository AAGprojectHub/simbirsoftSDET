from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
from datetime import datetime

class TransactionPage:
    def __init__(self, driver):
        self.driver = driver
        self.transaction_rows = (By.XPATH, "//table[@class='table table-bordered table-striped']//tbody//tr")
        self.date_column = (By.XPATH, ".//td[1]")
        self.amount_column = (By.XPATH, ".//td[2]")
        self.type_column = (By.XPATH, ".//td[3]")
    

    def get_transactions(self):
        rows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.transaction_rows)
        )
        
        transactions = []
        
        for row in rows:
            date_time = row.find_element(*self.date_column).text
            amount = float(row.find_element(*self.amount_column).text)
            transaction_type = row.find_element(*self.type_column).text
            transactions.append({
                'date_time': date_time,
                'amount': amount,
                'type': transaction_type
            })
        
        return transactions


    def save_transactions_to_csv(self, transactions, filename="transactions.csv"):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date-Time', 'Amount', 'Transaction Type'])
            
            for transaction in transactions:
                date_time = datetime.strptime(transaction['date_time'], "%Y-%m-%dT%H:%M:%S").strftime("%d %B %Y %H:%M:%S")
                writer.writerow([date_time, transaction['amount'], transaction['type']])


    def check_transactions(self, transactions):
        for transaction in transactions:
            if transaction['type'] not in ['Credit', 'Debit']:
                raise ValueError(f"Invalid transaction type: {transaction['type']}")