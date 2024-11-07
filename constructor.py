class Item:
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
    
item1 = Item("Phone", 100, -5)
item2 = Item("Laptop", 1000, 3) 

# print(item1.name)
# print(item1.price)
# print(item1.quantity)
# print(item2.name)
# print(item2.price)
# print(item2.quantity)

print(item1.claculate_total_price())
print(item2.claculate_total_price())

# You can even add more attribute of an instance of class after the instance is instanciated
item2.has_numpad = False

