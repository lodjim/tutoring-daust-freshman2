
class Account:
    def __init__(self):
        self.balance = 0
    
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
            print("The withdraw amount is",amount)
            print("new balance",self.balance)
        else:
            print("not enough in your balance")

    def deposit(self,amount):
        self.balance += amount
        print("the balance is ",self.balance)



nafissaAccount = Account()
parsineAccount = Account()
aminataAccount = Account()

print(nafissaAccount.balance)
nafissaAccount.deposit(1000)
print(nafissaAccount.balance)
nafissaAccount.withdraw(500)
print(nafissaAccount.balance)
