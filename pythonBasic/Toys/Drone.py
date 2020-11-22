from Toy import Toy

class Drone(Toy):
    def __init__(self):
        self.__wings = 0

    def __init__(self, product_num, name, price, wings):
        super().__init__(product_num, name, price)
        self.__wings = wings

    @property
    def wings(self):
        return self.__wings

    @wings.setter
    def wings(self, wings):
        self.__wings = wings