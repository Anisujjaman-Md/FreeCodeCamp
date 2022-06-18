class Item:
    #Class Atribute
    pay_rate = 0.8 #The Pay Rate is 0.8

    all = []

    def __init__(self, name : str, price : float,  quantity: int = 0):
        # Run validtion on the input
        assert price  >=0, f"Price {price} cannot be negative"
        assert quantity >= 0, f"Quantity {quantity} cannot be negative"

        #Assing to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        #Add to the all list
        self.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate #Item.pay_rate is the class attribute

    def __repr__(self):
        return f"Item('{self.name}', {self.price} {self.quantity})"

# print(Item.pay_rate)

# l = Item("Laptop", 1000,  20)
# print(Item.__dict__)
# print(l.__dict__)


# l.apply_discount()
# print(l.price)

# m = Item("Mobile", 100,  10)
# m.pay_rate = 0.9
# m.apply_discount()
# print(m.price)

item1 = Item("Laptop", 1000,  20)
item2 = Item("Mobile", 100,  10)
item2 = Item("Mouse", 500,  10)
item2 = Item("Watch", 100,  10)
item2 = Item("HeadPhone", 100,  10)

# for instance in Item.all:
#     print(instance.name, instance.price, instance.quantity)

print(Item.all)