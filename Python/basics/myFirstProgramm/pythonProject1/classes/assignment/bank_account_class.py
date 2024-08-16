"""
Exercise 8: Bank Account Class

Create a BankAccount class with attributes owner and balance.
Add methods deposit(amount) to increase the balance and withdraw(amount) to decrease the balance.
Add a __str__ method to print the account owner and balance.
Create a BankAccount object, perform some transactions, and print the final balance.
"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def __str__(self) -> str:
        return f'Owner : {self.owner} deposit : {self.balance}'


bank_account = BankAccount('Sonfack Gorgang', 100)
bank_account.deposit(100)

print(bank_account)
bank_account.withdraw(100)
print(bank_account)
bank_account.deposit(500)
print(bank_account)
