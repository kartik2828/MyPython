
# Question 2:
# Create a class `BankAccount` with attributes `account_number` and `balance`.
# Add methods `deposit(amount)` and `withdraw(amount)` to modify the balance.
# Ensure that the balance cannot go negative.

class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Initial balance is {self.balance}")

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if self.balance>=amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance. Transaction denied.")
obj = BankAccount(4521452132,5000)

obj.deposit(25600)

