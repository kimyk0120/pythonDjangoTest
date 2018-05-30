
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
print("############################################################")
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





























