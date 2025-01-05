class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withDraw = 100
        self.max_withDraw = 100000
    def get_balance(self):
        return self.balance   
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def withDraw(self,amount):
        if amount<self.min_withDraw:
            print(f"poor guy!you can withdraw below {self.min_withDraw}")
        elif amount>self.max_withDraw:
            print(f"woooahhh!!you can not withdraw more than {self.max_withDraw}")
        else:
            self.balance-=amount
            print(f"here is your money {amount}")
            print(f"your balance after withdraw {self.balance}")

        

brac = Bank(15000)
brac.withDraw(25)
brac.withDraw(5000)
brac.withDraw(20000000)
brac.withDraw(3500)
