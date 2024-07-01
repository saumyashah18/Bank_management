class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initial_ammount, acct_name):
        self.balance = initial_ammount
        self.name = acct_name
        print(f"\n Your Account of name {self.name} has been created \n Your Account has balance of ${self.balance: .2f}")
        
    def getBalance(self):
        print(f"\n Account : {self.name} \n balance : ${self.balance:.2f}")
 
    def deposit(self,ammount):
        self.balance = self.balance + ammount
        print("\n DEPOSIT COMPLETED")
    
        self.getBalance()
    
    def viableTransaction(self, ammount):
        if self.balance >= ammount:
            return
        else:
            raise BalanceException(
                f"\n Sorry your account of name {self.name} includes just the balance of {self.balance:.2f}"
            )

    def withdraw(self, ammount):
        try:
            self.viableTransaction(ammount)
            self.balance = self.balance - ammount
            print("Withdrawn Complete")
            self.getBalance()

        except BalanceException as error:
            print(f"\n Your Withdrawn has been interrupted : {error}") 

        
    def transfer(self, ammount, account):
        try:
            print("\n--------\nBegining transfer....")
            self.viableTransaction(ammount)
            self.withdraw(ammount)
            account.deposit(ammount)
            print("\n Your transfer has been completeddd!!!!")

        except BalanceException as error:
            print(f'\n Your transfer has been incompletee...{error}')

class Interestrewardacct(BankAccount):
    
     def deposit(self,ammount):
        self.balance = self.balance + (ammount*1.05)
        print("\n Your deposit has been completed....")
        self.getBalance()

class SavingsAcct(Interestrewardacct):
    
    def _init_(self,initial_ammount, acct_name ):
        super()._init_(initial_ammount,acct_name)
        self.fee = 5
    def withdraw(self,ammount):
        try:
            self.viableTransaction(ammount + self.fee)
            self.balance = self.balance -(ammount + self.fee)

            print("\n Withdraw completed!!!!¨")
            self.getBalance()

        except BalanceException as  error:
            print(f'\n Withdraw interrupted: {error}')


 

