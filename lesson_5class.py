print("1.--------------------------------------------------------------------")
'''1.  Створити список цілих чисел, які вводяться з терміналу та визначити серед них максимальне та мінімальне число.
'''
# i=0
# a=[]
# while i < 5:
#
#     b= int(input("Input numbers : "))
#     a.append(b)
#     i=i+1
# # a = [12,3,45,78]
# a = sorted(a)
# print(a)
# max = max(a)
# min= min(a)
#
# print("max =", max)
# print("min =", min)
#
# print("Variant 2----------------------------------------------------------")
#
#
# a=[]
# for i in range(5):
#     b = int(input("Input number:"))
#     a.append(b)
# a = sorted(a)
# print(a)
# max1 = max(a)
# min1 = min(a)
# print("max =", max1)
# print("min =", min1)
#
#
#
#
#
# print("Variant 3----------------------------------------------------------")
#
#
#
# i= int((input("Input numbers : ")))
#
# list1=[int(input("next number ")) for k in range(i)]
#
# print(list1)
# print("max", max(list1))
# print("min", min(list1))

print("2. ----------------------------------------------------")
'''В інтервалі від 1 до 10 визначити числа
•  парні, які діляться на 2,
•  непарні, які діляться на 3,
•  числа, які не діляться на 2 та 3.'''
# b=[]
# c=[]
# d=[]
#
# for i in range(1,11):
#     if i%2 == 0:
#         b.append(i)
#     elif i%3 == 0:
#         c.append(i)
#
#     else:
#         d.append(i)
#
# print("Parni", b)
# print("Ne Parni", c)
# print("Other", d)
#


# a= [’apple’, ’banana’, ’cherry’]
# x=12
#
# b=enumerate(a)
# # a.append(x)
# print(a)
# print(b)
#
# fruits = (1, 4, 2, 9, 7, 8, 9, 3, 1)
# x = fruits.count(9)
# print([1, 4, 2, 9, 7, 8, 9, 3, 1].index(9))


print("3. -----------------------------------------------------------")

'''Написати програму, яка обчислює факторіал числа, яке користувач вводить.(не використовувати рекурсивного виклику функції)'''

# n=int(input('Input number n: '))
# n=10
# a=1
#
# for i in range(1,n+1):
#     a=a*i
#     print(a)


print("4. -----------------------------------------------------------")
# ''' Напишіть скрипт, який перевіряє логін, який вводить користувач.
# Якщо логін вірний (First), то привітайте користувача.
# Якщо ні, то виведіть повідомлення про помилку.
# (використайте цикл while)'''
#
# login=input("Input your login: ")
#
#
# while login != 'test':
#
#     print("Incorrect login!!! ")
#     login=input("Try again to type your login: ")
# else:
#     print("Congratulation!!! You are a winner")