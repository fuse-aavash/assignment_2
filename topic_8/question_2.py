import random
class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance.")

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

    def __del__(self):
        print(f"Bank account with account number {self.account_number} is being closed.")


class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(self.generate_account_number(), 0, "Savings")

    def generate_account_number(self):
        
        
        return f"ACC-{random.randint(1000, 9999)}"

    def display_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        self.bank_account.display_details()

    def __del__(self):
        print(f"Customer {self.name} with account number {self.bank_account.account_number} is no longer a customer.")



customer1 = Customer("Aavash", 20, "Nepal")


customer1.display_details()


customer1.bank_account.deposit(1000)
customer1.bank_account.withdraw(500)


del customer1

