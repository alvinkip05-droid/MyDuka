from datetime import date

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0, date_opened=date.today()):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.date_opened = date_opened

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def display_info(self):
        print(" Account Information ")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")
        
        
        
 
account1 = BankAccount("001", "Alvin Kiplagat", 5000)
account2 = BankAccount("002", "Trisha Njoki", 12000)


account1.deposit(1500)
account1.withdraw(2000)
account1.display_info()

account2.deposit(3000)
account2.withdraw(5000)
account2.display_info()

   
