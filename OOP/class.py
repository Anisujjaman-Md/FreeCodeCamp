class Item:
    #Class Atribute
    pay_rate = 0.8 #The Pay Rate is 0.8


    def __init__(self, name : str, price : float,  quantity: int = 0):
        # Run validtion on the input
        assert price  >=0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        #Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity


    def calculate_total_price(self):
        return self.price * self.quantity

print(Item.pay_rate)

l = Item("Laptop", 1000,  2)
print(l.calculate_total_price())
