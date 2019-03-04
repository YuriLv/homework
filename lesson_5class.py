#
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

b=[]
c=[]
d=[]

for i in range(1,11):
    if i%2 == 0:
        b.append(i)
    elif i%3 == 0:
        c.append(i)

    else:
        d.append(i)

print("Parni", b)
print("Ne Parni", c)
print("Other", d)

