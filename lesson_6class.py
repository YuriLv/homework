# print('1. -----------------------------------------------------')
#
# list=[2,4,5,7]
# def avr(*arg):
#     a=0
#     for i in arg:
#         a= a+i
#     a=a/int(len(arg))
#     return a
#
# print(avr(3,5,6))
#
#
#
# print('2. -----------------------------------------------------')
#
# def abs(arg):
#     if arg>=0:
#         return arg
#
#     else:
#         return -arg
#
# print(abs(-7))
#
# print('3. -----------------------------------------------------')
#
#
#
# def maxi(a1,a2):
#     """Max of 2 digits:"""
#     if a1>a2:
#         return a1
#     elif a1==a2:
#         print("ERRROR")
#     else:
#         return a2
# print(maxi.__doc__)
# print (maxi(4,6))
#
# print('4. -----------------------------------------------------')
# # a=int(input("1- rect, 2 triangle, 3 cirkle. Pls input number: "))
# #
# # def rect(a1,a2):
# #     s=a1*a2
# #     return s
# #
# # def triang(a1,a2):
# #     s=(a1*a2)/2
# #     return s
# #
# # def cirkle(r):
# #     s=3.14*r*r
# #     return s
# #
# # if a==1:
# #     print("Rectangle square: ", rect(2,3))
# # elif a==2:
# #     print("Triangle square: ", triang(2,3))
# # elif a==3:
# #     print("Cirkle square: ", cirkle(2))
# #
# # else: print("Error input")


print('5. -----------------------------------------------------')
#
# arg=input("input number: ")
#
# def suma(arg):
#     s=0
#     for i in range(len(arg)):
#         i=int(arg[i])
#         s=i+s
#
#     return s
# print("Total suma of", arg, "is", suma(arg))

print('6. -----------------------------------------------------')
#
# a=int(input("input  a="))
# b=int(input("input  b="))
# # a=5
# # b=6
# inp=input("input +, -, * or / :")
#
# def s(a,b):
#     s=a+b
#     print("a+b=",s)
# def m(a,b):
#     m=a-b
#     print("a-b=", m)
# def c(a,b):
#     c=a/b
#     print("a/b=", c)
# def d(a,b):
#     d=a*b
#     print("a*b=", d)
#
# if inp=='+': s(a,b)
# elif inp=='-': m(a,b)
# elif inp =='*': d(a,b)
# elif inp=="/": c(a,b)
# else: print("Error operation !!!")


print('7. -----------------------------------------------------')
#
# n=int(input("Enter n. Fibo number:"))
# # n=11
#
# def f(n):
#     a=1
#     b=0
#     for i in range(n):
#         (a,b)=(b,a+b)
#
#     return b
#
#
#
# print("fibo =",f(n))


print('8. -----------------------------------------------------')
#
# print("axx+bx+c")
# print("D=bb-4ac")
# a=int(input("input a:"))
# b=int(input("input b:"))
# c=int(input("input c:"))
#
# def Des(a,b,c):
#     D=b*b-4*a*c
#     return D
# print("D=",Des(a,b,c))
# D=Des(a,b,c)
# print(D+26)
