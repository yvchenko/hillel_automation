import time

start = time.time()


class OurBilling:

    __order_numbers = []
    __allowed_types = ["apple", "orange", "calculator"]

    def __init__(self, order_number: int, quantity: int, total_price: float):
        if order_number in self.__order_numbers:
            order_number += time.time() - start
        self.__order_numbers.append(order_number)

        self.order_number = order_number
        self.quantity = quantity
        self.total_price = total_price
        self.__product_type = "default"

    @property
    def product_type(self):
        return self.__product_type

    @product_type.setter
    def product_type(self, value):
        if type(value) == str:
            if value in self.__allowed_types:
                self.__product_type = value
            else:
                raise IndexError
        else:
            raise ValueError("Incorrect type")

    def get_order_numbers(self):
        return self.__order_numbers

    def price_per_item(self):
        price_per_item = self.total_price // self.quantity
        return price_per_item


# order number
# product type
# quantity
# total price

    # available or not
    # actual amount
    # return price per item


first = OurBilling(0, 2, 200.0)
second = OurBilling(1, 3, 150.0)
third = OurBilling(0, 2, 4.5)
first.order_numbers = [1, 2, 3, 4]
print(first.order_numbers)
fifth = OurBilling(0, 0, 0)
print(third.get_order_numbers())

print(third.price_per_item())

print(first.product_type)
first.product_type = "apple"
print(first.product_type)

