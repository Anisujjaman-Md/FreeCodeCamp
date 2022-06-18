import csv
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
    
    #Class Method
    @classmethod
    def instantiate_from_csv(cls):
        with open("item.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get("price")),
                quantity = int(item.get("quantity")),
            )    

    def __repr__(self):
        return f"Item('{self.name}', {self.price} {self.quantity})"

Item.instantiate_from_csv()
print(Item.all)