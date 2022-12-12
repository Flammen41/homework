###### Task1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade_level):
        super().__init__(name)
        self.grade_level = grade_level

    def attend_class(self):
        print('Student {} is attending class.'.format(self.name))

class Teacher(Person):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def assign_homework(self):
        print('Teacher {} is assigning homework.'.format(self.name))

################################################################
###### Task 2












################################################################
###Task3
class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Product should be an instance of Product class")
        self.products.append(product)

    def remove_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Product should be an instance of Product class")
        if product not in self.products:
            raise ValueError("Product is not in the store")
        self.products.remove(product)

    def get_total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Product should be an instance of Product class")
        if product not in self.products:
            raise ValueError("Product is not in the store")
        product.price += product.price * 0.3
        product.amount += amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type == 'name':
            for product in self.products:
                if product.name == identifier:
                    product.price *= (1 - percent / 100)
        elif identifier_type == 'type':
            for product in self.products:
                if product.type == identifier:
                    product.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        for product in self.products:
            if product.name == product_name and product.amount >= amount:
                product.amount -= amount
                self.income += product.price * amount
                return
        raise ValueError("Product is not in the store or amount is not available")

    def get_income(self):
        return self.income

    def get_all_products(self):
        info = []
        for product in self.products:
            info.append((product.name, product.amount))
        return info

    def get_product_info(self, product_name):
        for product in self.products:
            if product.name == product_name:
                return (product.name, product.amount)
        raise ValueError("Product is not in the store")

################################
#Task4
class CustomException(Exception):

def __init__(self, msg):
    self.msg = msg
    with open('logs.txt', 'a') as f:
        f.write(f'{msg}\n')
    super().__init__(msg)