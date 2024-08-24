class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate # this will search for the attribute at the instance level first 
        # and if it doesn't find it, it will search at class level
        # but writing Item.pay_rate instead of self.pay_rate, will override this search and access pay_rate attribute at the class level
    

    # magic method to change the representation of each instance 
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
        # it's a part of best practices to keep the instance representation similar to the way they are created

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

# prints the list contaning instance memory addresses (references)
print(Item.all)

# to print the names of all items
for instance in Item.all:
    print(instance.name)
