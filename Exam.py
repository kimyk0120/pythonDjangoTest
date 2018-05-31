
import egoing

# a = 1
b = 2
# if a > b:
    # print("1")
# elif a < b:
    # print("2")
# else:
    # print("3")
# print("4")

# in_str = input("Key input : ")
# print(in_str)
# in_str = input("id input.\n")

real_egoing = "egoing"
real_k8805 = "k8805"

# if real_egoing == in_str or real_k8805 == in_str:
#   print("Hello!")
# else:]
#   print("Who are you?")
# print("############################################################")
'''
multiple annotation
'''
# print(type('egoing'))
# print(type(['tst1','tst2','tst3']))
# egoing = ['programmer', 'seoul', 25, False]
# print(egoing)


def fTest(a):
    print("ftest : " + str(a))
# fTest(1)


testList = ["1","2","3"]
tesLIstis = "1" in testList
# print(tesLIstis)
# print(len(testList))


'''
i = 0
while i < 3:
    print('while test')
    i = i + 1

i = 0
while i < 10:
    if i == 4:
        break
    print(i)
    i = i + 1
print('after while')
'''

members = ['egoing', 'leezche', 'graphittie']
i = 0
# while i < len(members):
#     print(members[i])
#     i = i + 1


def a3():
    return 'AAA'
# print(a3())
# math.sqrt()
# print(sys.path)

# print(egoing


class MyClassTestTestTest:
    pass


class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def add(self):
        return self.v1 + self.v2

    def subtract(self):
        return self.v1 - self.v2


c1 = Cal(10,20)
c1result = c1.add()
c1result2 = c1.subtract()
# print(c1result)
# print(c1result2)
c1.v1 = 50
# print(c1.v1)
# print(c1.subtract())
# c2 = Cal(30, 20)
# print(c2.add())
# print(c2.subtract())

'''
new-style 클래스와 old-style클래스의 차이

Python 3.x:

class MyClass(object): new-style 클래스
class MyClass: new-style 클래스 (명시하지 않아도 자동으로 상속)
'''


class CLass1(object):
    def method1(self):
        return 'm1'


c1 = CLass1()
# print(c1, c1.method1())


class Class3(CLass1):
    def method2(self): return 'm2'


class CLass2(object):
    def method1(self):
        return 'm1'

    def method2(self):
        return 'm2'


c2 = CLass2()
# print(c2,c2.method1())
# print(c2,c2.method2())

c3 = Class3()
# print(c3,c3.method1())
# print(c3,c3.method2())


class Cs:
    @staticmethod
    def static_method():
        print("Static method")
    @classmethod
    def class_method(cls):
        print("Class method")
    def instance_method(self):
        print("Instance method")


# i = Cs()
# Cs.static_method()
# Cs.class_method()
# i.instance_method()


class Cs:
    count = 0

    def __init__(self):
        Cs.count = Cs.count + 1

    @classmethod
    def getCount(cls):
        return Cs.count


i1 = Cs()
i2 = Cs()
i3 = Cs()
i4 = Cs()
# print(Cs.getCount())





class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        if isinstance(v1, int):
            self.v1 = v1
        if isinstance(v2, int):
            self.v2 = v2
    def add(self):
        result = self.v1+self.v2
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    def subtract(self):
        result = self.v1-self.v2
        Cal._history.append("subtract : %d-%d=%d" % (self.v1, self.v2, result))
        return result
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
    def getV1(self):
        return self.v1
    @classmethod
    def history(cls):
        for item in Cal._history:
            print(item)
class CalMultiply(Cal):
    def multiply(self):
        result = self.v1*self.v2
        Cal._history.append("multiply : %d*%d=%d" % (self.v1, self.v2, result))
        return result
class CalDivide(CalMultiply):
    def divide(self):
        result = self.v1/self.v2
        Cal._history.append("divide : %d/%d=%d" % (self.v1, self.v2, result))
        return result
# c1 = CalMultiply(10,10)
# print(c1.add())
# print(c1.multiply())
# c2 = CalDivide(20,10)
# print(c2, c2.add())
# print(c2, c2.multiply())
# print(c2, c2.divide())
# Cal.history()


class C1:
    def m(self):
        return 'parent'


class C2(C1):
    # pass
    def m(self):
        return super().m() + ' child'
    pass


o = C2()
print(o.m())
















