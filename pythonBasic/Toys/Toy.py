class Toy(object):
    def __init__(self):
        self.__product_num = ''
        self.__name = ''
        self.__price = 0

    def __init__(self, product_num, name, price):
        self.__product_num = product_num
        self.__name = name
        self.__price = price

    @property
    def product_num(self):
        return self.__product_num

    @product_num.setter
    def product_num(self, product_num):
        self.__product_num = product_num

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price


