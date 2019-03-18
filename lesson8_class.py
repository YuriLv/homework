'''Створити батьківський клас Figure з методами init: ініціалізується колір,
get_color: повертає колір фігури,
info: надає інформацію про фігуру та колір,  від якого наслідуються такі класи як Rectangle, Square,
які мають інформацію про ширину, висоту фігури, метод square, який знаходить площу фігури.'''

class Figure:
    def __init__(self, color,figuretype):
        self.color=color
        self.figuretype = figuretype

    def get_color(self):
         print('Color is' + ' ' + self.color)
         return self.color

    def info(self):

        print('Figure type is ' + self.figuretype +', '+ 'color is ' + self.color)

class Rectangle(Figure):
    def __init__(self,color,figuretype,x,y):
        super().__init__(color,figuretype)
        self.x = x
        self.y = y

    def square(self):
        a=self.x * self.y
        print("Square of "+ self.figuretype + ' is '+ str(a))

class Square(Figure):
    def __init__(self,color,figuretype,x):
        super().__init__(color,figuretype)
        self.x = x


    def square(self):
        a=self.x * self.x
        print("Square of "+ self.figuretype + ' is '+ str(a))



triang= Figure("blue","triangle")
rectan =Rectangle('white','rectangle',4,8 )
squar= Square('red', 'square',5)


triang.get_color()
triang.info()
rectan.info()
rectan.square()
squar.info()
squar.square()






class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # def __str__(self):
    #     c =str((self.a, self.b))
    #     return c
    def __add__(self, other):
        k= Vector(self.a + other.a, self.b + other.b)
        return k



v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)





# class A:
#     def __init__(self,x):
#         self.x = x
#
#     def myMethod(self):
#
#         return self.x**2
#
# try1=A(6)
#
# print(try1.myMethod())
#


# class Hero:
#     def __init__(self,name,level):
#         self.name = name
#         self.level = level
#         self.health = 100
#
#     def show(self):
#         desc =("Name " + self.name + " " + "level" + " " + str(self.level) +", health =" + str(self.health)).title()
#         print(desc)
#
#     def levelup(self):
#         self.level+=1
#
#     def sethealth(self,newhealth):
#         self.health = newhealth
#
#
#
# hero1=Hero('Vasja',1)
#
# hero1.show()
# hero1.levelup()
# hero1.health=90  #-- bad practise
# hero1.show()
# hero1.sethealth(60)
# hero1.show()



