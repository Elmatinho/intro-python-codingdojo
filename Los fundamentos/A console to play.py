class User:
    def __init__(self,username,email_address):
        self.name=username
        self.email=email_address
        self.account_balance=0
    

    def make_deposit(self, amount):
        self.account_balance += amount
        
    def make_withdraw(self,amount):
        self.account_balance -=amount
    
    def display_user_balance(self):
        print(self.name,self.account_balance)
    
   # @staticmethod
    #def transfer(for_destin,amount):
     #   print(for_destin.account_balance,amount)
    
        

matias=User("Matías", "matias@email.com","Matías", "matias@email.com")
cecilia=User("Cecilia","cecilia@email.com","Matías", "matias@email.com")
cynthia=User("Cynthia","Cynthia@email.com","Matías", "matias@email.com")
matias.make_deposit(100)
matias.make_deposit(300)
matias.make_deposit(100)
matias.make_withdraw(50)
matias.display_user_balance()
cecilia.make_deposit(100)
cecilia.make_deposit(100)
cecilia.make_withdraw(50)
cecilia.make_withdraw(50)
cecilia.display_user_balance()
cynthia.make_deposit(1000)
cynthia.make_withdraw(150)
cynthia.make_withdraw(150)
cynthia.make_withdraw(150)
cynthia.display_user_balance() 
