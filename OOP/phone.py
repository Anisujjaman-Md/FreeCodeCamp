from item import Item

class Phone(Item):
    def __init__(self, name : str, price :float, quantity : int = 0, broken_phone : int = 0):
        super().__init__(name, price, quantity)
        #Run validtion on the input
        assert broken_phone >= 0, f"Broken Phone {broken_phone} cannot be negative or zero"
        #Assign to self object
        self.broken_phone = broken_phone