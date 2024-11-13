class Bank:
    bankName = "Bank of Baroda"
    branch = "Benguluru"

    #create account
    def __init__(self, userName, pan, address):
        self.userName = userName
        self.pan = pan
        self.address = address
        self.balance = 0.0
        print(f'hello {self.userName} cong! your account created successfully ')
      
    #deposit
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'{amount} deposited successfully')

    #withdraw
    def withdraw(self,amount):
        if amount <self.balance :
            self.balance=self.balance-amount 
        else:
            print('Insufficent Fund....')  

     #Mini statement
    def ministatement(self):
        print(f'your account balance is {self.balance}')


print(f'Welcome to {Bank.bankName} , {Bank.branch}')
userName = input('Enter Your name : ')
pan = input('Enter Pan Card number : ')
address = input('Enter Your address : ')

b = Bank(userName, pan, address)

while True:
    print('Please Select any Option : ')
    print('1.Deposite\n2.Withdraw\n3.Ministatement\n4.Stop')
    option = int(input(" "))

    if option==1:
        amount=float(input('Enter Deposited amount :'))
        b.deposit(amount)

    if option==2:
        amount=float(input('Enter withdraw amount :'))
        b. withdraw(amount)

    if option==3:
        b.ministatement()   

    if option==4:
        print('Thanks for using bank of baroda....')  
        break  