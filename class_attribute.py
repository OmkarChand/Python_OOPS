# Class attributes are the attributes which we can use to share amont the different instances of the class or directly as a class attribute.

class Item:
    # Class attributes
    pay_rate = 0.8 # The pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def claculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
    
item1 = Item("Phone", 100, 5)

# How to access the class attributes using class
print(Item.pay_rate)

# Accessing the class attribute using instances
print(item1.pay_rate)

# Magic keyword to print all the attributes belonging to the object
print(Item.__dict__) # show the result in dictonary format
print(item1.__dict__) 

# Price after discount
item1.apply_discount()
print(item1.price)

# I want to apply different discount for item2 = laptop, if I change the class attribute then it will affect to all instances, 
# so its better to create the pay_rate at instance leve for the item2
item2 = Item("Laptop", 1000, 3) 
item2.pay_rate = 0.7 # 30% discount

# Price after discount
item2.apply_discount()
print(item2.price)

