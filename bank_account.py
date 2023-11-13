#an exception is called if there is a problem with the balance and its not enough to withdraw
class BalanceException(Exception):
    pass #

class BankAccount:
    def __init__(self,initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName 
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")


    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self,amount):
        self.balance = self.balance + amount
        print("\Deposit Completed")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self,amount):
        try: 
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw Interrupted : {error}')

    def transfer(self,amount, account):
        try: 
            print('\n *****************\n\n Beginning Transfer 💸💸💸💸 ')
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\n Transfer Complete! ✅ \n\n *************')
        except BalanceException as error:
            print(f'\n Transfer Interrupted. ❌ {error}')

#the class we are inheriting from is Bank Account 
class InterestRewardsAcct(BankAccount):
    #override the deposit acct so they gain more money
    def deposit(self,amount):
        self.balance = self.balance + (amount * 1.05)
        print ("\n Deposit complete ")
        self.getBalance()
#inherits from InterestRewardsAcct
class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee =  5 
    
    #ovverrride 
    def withdraw(self, amount):
        try: 
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee )
            print("\n Withdraw Compelete")
            self.getBalance()
        except BalanceException as error: 
            print (f'\n Withdrawl Interrupted: {error}')
