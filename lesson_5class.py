 # a= (input("Input numbers : "))
i=0
d=[]
a=[]
while i < 5:

    b= int(input("Input numbers : "))
    a.append(b)
    i=i+1
# a = [12,3,45,78]
b= sorted(a)
print(b)
max = max(a)
min= min(a)

print(max)
print(min)

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
a = range(1,11,1)
for i in a:
    if i%2 == 0:
        b.append(i)
    elif i%3 == 0:
        c.append(i)

    else:
        d.append(i)

print("b=", b)
print("c=", c)
print(d)


        # else:
    #     d= not c and not b
    #     print(d)
# print("b=", b)
# print("c=", c)
