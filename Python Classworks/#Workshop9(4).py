from datetime import datetime

class BankAccount:
    def __init__(self, account_number, customer_name, initial_deposit):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = initial_deposit
        self.date_of_opening = datetime.now()

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successful. New balance is {self.balance}")

    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: {self.balance}")
        print(f"Date of Opening: {self.date_of_opening}")

# Creating an instance of the BankAccount class
my_account = BankAccount("123456789", "Chantal Momah", 300000)

# Performing transactions and checking balance
my_account.deposit(50000)
my_account.withdraw(20000)
my_account.check_balance()
