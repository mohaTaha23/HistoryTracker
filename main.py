# import time
# import math
# import numpy as p
from classes import Car

#
# # ina = input("what is ur age? : ")
# # ina = int(ina)
# # print(type(ina))
# # print("ur name in reverse:" + ina[::-1])
#
# arr = ["first","second","etc"]
# print(arr)

# if and elif
# if len(arr) >=2 and len(arr) <=10 :
#     print(arr.sort())
# elif len(arr) == 11:
#     print("yess")
# else:
#     print("ok")
#=======================================

# while loop
# name = None
# while not name:
#     name = input("enter ur name")
# print("hello "+name)
# ======================================

#for loop

# for i in range (0,10):      # note its excluded
#     print(i+1)
#
# for i in range (10,0):
#     print(i)
#
# for i in p.arange(0,-10,-0.5):
#     print(i)
#===============================

#   dic (more like hashmap)
# map = {
#     "first" : "sunday",
#     "second" : "monday",
#     "third" : "TUESDAY"
# }
#
# print(map['first'])
#===============================

#  func ( def)
# def func(number) :
#     return  number**2

#===============================
# sl = slice(10,20)
# print(type(sl))
#
# print(int(False *10))

#  ex:
# for i in range(5):
#     for j in range(10):
#         print("#",sep="",end=" ")
#     print("")
# ========================================

# array
# food = ["apple","milk","cake","timasue","cheesecake"]
#  =======================================

# name = "taha"
# def change_name():
#     name = "Rami"
#     global name # doesnt work, should delete the local one
#     name=name
#
# print(name)

# ==========================================

#  * args
# def sum (* args):
#     values = list(args)
#     result =0
#     for value in values:
#         result+=value
#     return result
# print(sum(1,2,3,4,5))
#  =========================================

# exception handling
# try:
#     raise Exception()
# except Exception:
#     print("if error")
# else:
#     print("if no error")
# finally:
#     print("always done")

# =========================================

# 2 dim array

# arr = [1][1]
# print(arr)

# ==========================================
#
# def sth (**kwargs):
#     for l in kwargs:
#         print(kwargs[l] ,end=" ")
#
# sth(name = 21) #  accepts keyword args only , not positional

# ============================================

#  objects from classes in a diff module / imported them

# my_car.calc(5,6)
# my_car.walk()

# mycar = Car("hema",12,"no one")
# print(mycar.driver)



# class Film:
#     def __init__(self, name="", actors_number=0, duration=0):
#         self.name = name
#         self.actors_number = actors_number
#         self.duration = duration


class Animal :
    def __init__(self, name="", age=0, color=""):
        self.name = name
        self.age = age
        self.color = color

    def eat(self):
        print(self.name + " is eating")

    def sleep(self):
        print(self.name + " is sleeping")

    def info(self):
        print("name: "+self.name + " age: "+str(self.age) + " color: "+self.color)
class Fish(Animal):

    def swim(self):
        print(self.name + " is swimming")

class Peranna(Fish,Animal):
    pass


popo = Peranna("popo", 2, "red")
popo.swim()