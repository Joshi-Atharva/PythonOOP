import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!"

        # Assign to self object
        self.__name = name # __ before the attribute name signifies private attribute - something that cannot be accessed from instance level
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)

    @property
    # Property Decorator = Read-Only Attribute
    # It looks like a function (method) but with the @property decorator before it, it behaves like an attribute with its value as written after return statement
    # but it will also behave like a function. It'll execute all the statements before the return statement 
    def name(self):
        return self.__name

    # in case you ask what is the need for assigning a property and then using setter if we can update the value from instance level then read the following:
    '''
    Setters are methods in object-oriented programming languages that update the value of an object's attribute.
    They are also known as mutators. Setters can be used to protect data, especially when creating classes. 
    They can also be used to apply constraints to ensure that the 'new' values assigned to the attributes are 'valid'
    emphasis on 'new': these constraimts are not enoforced during initial assignment (initialisation/ instantiation)
    '''

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"
