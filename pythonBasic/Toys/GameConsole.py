from Toy import Toy

class GameConsole(Toy):
    def __init__(self):
        self.__portable = False

    def __init__(self, product_num, name, price, portable):
        super().__init__(product_num, name, price)
        self.__portable = portable

    @property
    def portable(self):
        return self.__portable

    @portable.setter
    def portable(self, portable):
        self.__portable = portable

