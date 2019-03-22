print('1. ----------------------------------------------------')
'''Regular Ball Super Ball
Create a class Ball.
Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"

'''

class Ball:

    def __init__(self,type='regular'):
        self.type=type


    def ball_type(self,type='regular'):
        
        print(self.type)




    # def ball_type(self,type):
    #     self.type=type
    #     print("super")

    #
    # def __init__(self,type=None):
    #     self.type =
    #
    # def ball_type(self):
    #     print("regular")
    #
    # def ball_type(self,type):
    #     self.type=type
    #     print("super")



ball1= Ball("super")
ball2 =Ball()
ball1.ball_type()
ball2.ball_type()
#
# print('2. ----------------------------------------------------')
# '''According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
#
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes'''
#
# class Human:
#     def __init__(self,hair,weight,hight):
#             self.hair = hair
#             self.weight = weight
#             self.hight = hight
#
#
# class Men(Human):
#
#     def __init__(self,hair, weight,hight,trauses):
#         super().__init__(hair,weight,hight)
#         self.trauses = trauses
#
# class Women(Human):
#
#
#     def __init__(self, hair, weight, hight, tshirt):
#         super().__init__(hair, weight, hight)
#         self.tshirt = tshirt
#
#
# print('3. ----------------------------------------------------')
# '''Color Ghost
#
# Create a class Ghost
#
# Ghost objects are instantiated without any arguments.
#
# Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated
#
# ghost = Ghost()
# ghost.color  #=> "white" or "yellow" or "purple" or "red"'''
#
# from random import *
# class Ghost:
#
#     def color(self):
#
#         foo = ['a', 'b', 'c', 'd', 'e']
#
#         colors = ["white", "yellow", "purple", "red"]
#
#         for x in range(4):
#             i = randrange(0, 4)
#         return colors[i]
#
# ghost = Ghost()
# print(ghost.color())
#
#
# print('4. ----------------------------------------------------')
# '''Classy Classes
# Basic Classes, this kata is mainly aimed at the new JS ES6 Update introducing classes
# Task
# Your task is to complete this Class, the Person class has been created. You must fill in the Constructor method to accept
#  a name as string and an age as number, complete the get Info property and getInfo method/Info getter which should return
# johns age is 34
# '''
#
# class Person:
#     def __init__(self,name,age):
#         self.name=str(input("input name: "))
#         self.age=int(input("input age: "))
#
#     def get_info(self):
#         print(self.name+" age is ",self.age)
#
# johny =Person("john",34)
#
# johny.get_info()
