from item import Item
from phone import Phone
from keyboard import Keyboard

# Item.instantiate_from_csv()

# phone1 = Phone("Iphone", 5000, 1, 1)
# phone2 = Phone("Android", 1000, 1, 1)

# print(Item.all)
# print("----------------------------------------------------")
# print(Phone.all)
# Item.instantiate_from_csv()
# print(Item.all)

# item1 = Item("Iphone", 5000, 1)

# item1.name = "Iphone X"

# item1.apply_discount()
# item1.apply_increment(0.2)
# print(item1.price)

item1 = Item("Asus Laptop", 1000, 1)
item2 = Phone("Android", 1000, 1)
item3 = Keyboard("Logitech", 1000, 1)

print(f"Item: {item1.price} Phone:{item2.price} Keyboard: {item3.price}")

#Polymorphism example
#Same method name but different implementation

item1.apply_discount()
item2.apply_discount()
item3.apply_discount()

print(f"Item: {item1.price} Phone:{item2.price} Keyboard: {item3.price}")