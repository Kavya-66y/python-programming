class Account():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"current balance after deposit is {self.balance}")
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print(f"withdrawl amount is {wd_amt}")
        else:
            print("sorry! funds not available")
    def __str__(self):
        return f"owner name is {self.owner}\nbalance is {self.balance}"
a = Account("kavya",5000)
print(a)
deposit = a.deposit(1000)
print(f"current balance is {a.balance}")
withdraw = a.withdraw(3000)
print(f"current balance  is {a.balance}")
    
        