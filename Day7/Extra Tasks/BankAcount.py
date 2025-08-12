class Bank:
    def __init__(self, Owner="none", Balance=0):
        self.Owner = Owner
        self.Balance = Balance

    def Deposit(self, amount):
        if amount > 0:
            self.Balance += amount
            print(f"Deposited {amount}. New Balance: {self.Balance}")
        else:
            print("Invalid deposit amount!")

    def Withdraw(self, amount):
        if amount > 0:
            if amount <= self.Balance:
                self.Balance -= amount
                print(f"Withdrawn {amount}. New Balance: {self.Balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount!")

    def GetBalance(self):
        return self.Balance


Bank1 = Bank("Faisal", 400)
Bank1.Deposit(150)   
Bank1.Withdraw(55)   
print("Current Balance:", Bank1.GetBalance())
