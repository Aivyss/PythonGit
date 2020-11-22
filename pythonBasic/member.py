class Parent:
    word = "상속 전: "

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    @staticmethod
    def static_method():
        print("Static method")

    @classmethod
    def class_method(cls):  # cls의 첫 매개변수가 요구됨.
        print(cls.word+"Class method")

    def instance_method(self):  # self 첫 매개변수가 요구됨.
        print("Instance method")


class Child(Parent):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


i = Parent(1, 2)
j = Child(3, 4)

i.static_method()
j.static_method()

i.class_method()
j.class_method()
