from ToyManager import ToyManager
from Toy import Toy
from Bycicle import Bycicle
from GameConsole import GameConsole
from Drone import Drone

class ToyUI(object):
    def __init__(self):
        self.__mgr = ToyManager()

        while True:
            print('=== Toy Manager ===')
            print('1. 장난감 등록')
            print('2. 장난감 검색')
            print('3. 장난감 삭제')
            print('4. 장난감 검색')
            print('5. 장난감 정보출력')
            print('9. 종료')
            selector = int(input('선택: '))

            if selector == 1:
                ToyUI.add()
            elif selector == 2:
                ToyUI.search()
            elif selector == 3:
                ToyUI.delete()
            elif selector == 4:
                ToyUI.price_search()
            elif selector == 5:
                ToyUI.info_show()
            elif selector == 9:
                print("종료")
                break
            else:
                print('[에러] 잘못 입력했습니다.')

    @classmethod
    def add(cls):
        pass
    @classmethod
    def search(cls):
        pass
    @classmethod
    def delete(cls):
        pass
    @classmethod
    def price_search(cls):
        pass
    @classmethod
    def info_show(cls):
        pass