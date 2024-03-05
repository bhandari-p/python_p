# create a account class and methods to  debit, creadit and print balance
class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def credit(self,amount):
        self.balance +=amount
        print("Rs",amount,"was credited to your account")
        

    def debit(self,amount):
         self.balance -=amount
         print("Rs",amount,"Was debited from your account")
        

    def balance_check(self):
        print("your account balance is Rs",self.balance)

ac1=Account("Prajwal",10000)
ac1.credit(2000)
ac1.debit(1200)
ac1.balance_check()