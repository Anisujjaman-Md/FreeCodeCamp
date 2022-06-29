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
        self.__name = name
        self.price = price
        self.quantity = quantity

        #Add to the all list
        self.all.append(self)

    @property
    #Getter/ Property Decorator = Read-Only Atribiutes
    def name(self):
        return self.__name

    @name.setter
    #Setter/ Property Decorator = Write-Only Attributes
    def name(self, value):
        self.__name = value


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate #Item.pay_rate is the class attribute
    
    #Class Method
    @classmethod
    def instantiate_from_csv(cls):
        with open('D:\Practice\FreeCodeCamp\OOP\items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get("price")),
                quantity = int(item.get("quantity")),
            )   #Item.instantiate_from_csv() is the class method

    @staticmethod
    def is_integer(number):
        #We will count the float that are point zero
        if isinstance(number, float):
            return number.is_integer()
        elif isinstance(number, int):
            return True
        else:
            return False
        
    def __repr__(self):       
        return f"{self.__class__.__name__}('{self.name}', {self.price} {self.quantity})"
 