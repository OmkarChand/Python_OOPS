# Class definition
class item:

    # Constructor
    def __init__(self):
        pass
    # Methods creation
    def calculate_total_price(self, x, y):
        return x * y

# Object creation of the class item
item1 = item()      
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = item()      
item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price(item2.price, item2.quantity))

# Printing the types of above variables
# print(type(item1))          # item
# print(type(item1.name))     # str
# print(type(item2.calculate_total_price))    # class method

