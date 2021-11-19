class TestClass:
    def __init__(self):
        self.__var1 = 10
        self.__var2 = 20

    def set_var1(self,value):
        self.__var1 = value

    def get_var1(self):
        return self.__var1

    def set_var2(self, value):
        self.__var2 = value

    def get_var2(self):
        return self.__var2


a = TestClass()
b1 = a.get_var1()
b2 = a.get_var2()
print(b1, b2)
a.set_var1(11)
a.set_var2(22)
c1 = a.get_var1()
c2 = a.get_var2()
print(c1, c2)

