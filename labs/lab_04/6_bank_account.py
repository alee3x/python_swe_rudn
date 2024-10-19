class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance


account1 = BankAccount(account_number=123, balance=0)

print(f"Account number: {account1.account_number}, Current balance: {account1.balance}")
print(f"Current balance: {account1.deposit(50)}")
print(f"Current balance: {account1.withdraw(10)}")
