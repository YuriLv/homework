# '''x = [1, 2, 3]
# y = x
# print (x)             # [1, 2, 3]
# y += [3, 2, 1]
# print (x)             # [1, 2, 3, 3, 2, 1]
#
# print(y)
#
# print("-------------------------")
#
# x = [1, 2, 3]
# y = x
# print (x)             # [1, 2, 3]
# y = y + [3, 2, 1]
# print ("x=", x)             # [1, 2, 3, 3, 2, 1]
#
# print("y=", y)
# '''
print("1.--------------------------------------------------------")

a= 0
while a<40:
    a=a+2
    print (a)

print()

for a in range(0,40,2):
    print(a)

print("--------------------------------------------------------")

for a in range(1,40,2):
    print(a)

print("2.--------------------------------------------------------")


for a in range (40):
    if a%2 == 0:
        continue
    print(a)

print("3.--------------------------------------------------------")


a =[4,2,6,8,12,14,18,522,3]
s=False

for i in a:
    if not i%2 == 0:
        s=True
        print ("number", i)
        break
if s==False:
    print("No odd")




print("4. --------------------------------------------------------")

a = [2,5,6,7,5,3,6]
for i in range(len(a)):
    a[i] = float(a[i])
print (a)

print("5. --------------------------------------------------------")
'''5.  Вивести числа Фібоначі включно до введеного числа n, використовуючи цикли. (Послідовність чисел Фібоначі 0, 1, 1, 2, 3, 5, 8, 13 і т.д.)
'''


n=int(input("Input max number N1: "))
# n=21
a=0
b=1
for i in range(0,n):
    print(a)
    (a,b) = (b,a+b)


    if a<=n:
        continue
    else:
        break


n=int(input("Input max number N2: "))
# n=21
a=0
b=1

while a<=n:
    print(a)
    (a, b) = (b, a + b)


n=int(input("Input max number N3: "))
n=21
a=0
b=1

while a<=n:
    print(a)
    t = a
    a = b
    b = t + a

