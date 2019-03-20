
print('1. ----------------------------------------------------')
'''1.  Напишіть програму, яка пропонує користувачу ввести ціле число і визначає чи це число парне чи непарне, чи введені дані коректні.
'''
# try:
#     x=int(input("Please enter a number:"))
#     if x==0:
#         print("number is 0")
#
#     elif x%2==0:
#         print("number is odd")
#
#     else:
#         print("number is not odd")
#
# except ValueError:
#     print("Its not a number. Input only digits")

print('2. ----------------------------------------------------')
'''2.  Напишіть програму, яка пропонує користувачу ввести свій вік, після чого виводить повідомлення про те чи вік є парним чи непарним числом. 
Необхідно передбачити можливість введення від’ємного числа, в цьому випадку згенерувати власну виняткову ситуацію. 
Головний код має викликати функцію, яка обробляє введену інформацію.'''

def age():
    try:
        x=int(input("Please enter your age:"))
        if x==0:
            print("Your age cant be 0")
        elif x<0:
            raise Exception("Minus input")
        elif x>120:
            raise Exception("Too high")
        elif x%2==0:
            print("Your age is odd")
        else:
            print("Your age is not odd")

    except ValueError:
        print("not valid number. Should be only digits")

    except Exception:
        print("Minus input ERROR")
    except  Exception as e:
        print("Your age is too high, input correct age")

    return

age()


print('3. ----------------------------------------------------')
'''3.  Напишіть програму для обчислення частки двох чисел, які вводяться користувачем послідовно через кому, передбачити випадок ділення на нуль, 
випадки синтаксичних помилок та випадки інших виняткових ситуацій. Використати блоки else та finaly.
'''

#
# try:
#     a, b = eval(input("input a,b:"))
#     print(a, b)
#     ost=a//b
#     print(ost)
#
#
# except ValueError:
#     print("not valid number. Try again later...")
# except ZeroDivisionError:
#     print("Devision by zero. Try again later...")
# except NameError:
#     print( "should be a number, not text")
# except SyntaxError:
#     print("Should be separeted with comma ")
# else:
#     print("No exception")
# finally:
#     print("Bye Bye")

print('4. ----------------------------------------------------')
'''Написати  програму, яка аналізує введене число та в залежності від числа видає день тижня, який відповідає цьому числу (1 це Понеділок, 2 це Вівторок і т.д.) . 
Врахувати випадки введення чисел від 8 і більше, а також випадки введення не числових даних.'''
#
# try:
#
#     week =["Monday", "Tuesday", "wednesday", "thursday", "friday", "saturday", "SUNDAY"]
#     day=int(input("Input number of day from 1 to 7:"))
#     if day >7 or day < 1:
#         raise Exception("Not correct day")
#
# except ValueError:
#     print("not text, should be number from 1 to 7")
#
# except Exception:
#     print("Error! Input digits from 1 to 7")
#
# else:
#     print("The day is ",week[day - 1])