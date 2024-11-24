class UPI:

    def __init__(self, username):
        self.username = username

    def make_payment_to(self, amount, account):
        print(f"{self.username} paying {amount} to {account} ...")

    def transaction_history(self):
        print(f"displaying transaction of {self.username}...")


class Gpay(UPI):
    def __init__(self, username):
        super().__init__(username)

    def get_a_loan(self, amount):
        print(f"{self.username} getting  a loan of amount {amount}...")

    def Pay_water_bill (self, bill_no, amount):
        print(f"{self.username} paying {amount} for water bill with number{bill_no}")



class Phonepe(UPI):
    def __init__(self, username):
        super().__init__(username)        

    def get_bike_insurance(self):
        print(f"{self.username} availing bike insurance....")

    def book_a_flight(self):
        print(f"{self.username} booking a flight ...")

user1 = Gpay("kiran")
user1.make_payment_to(500, "Account123")        
user1.get_a_loan(1000)

user2 = Phonepe("Amit")

user2.book_a_flight()
user2.get_bike_insurance()

