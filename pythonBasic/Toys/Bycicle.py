from Toy import Toy

class Bycicle(Toy):
    def __init__(self):
        self.__type = ''

    def __init__(self, product_num, name, price, type):
        Toy.__init__(product_num, name, price)

        if type == 1:
            self.__type = '도로용'
        elif type == 2:
            self.__type = '산악용'

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type):
        if type==1:
            self.__type = '도로용'
        elif type==2:
            self.__type = '산악용'
