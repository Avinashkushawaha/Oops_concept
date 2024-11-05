# Create a class called Order which stores item & its price.use Dunder function _ _gt _ _() to convey that: order1> order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price

ord1 = Order("chips", 20)        
ord2 = Order("tea", 15)

print(ord1 > ord2)