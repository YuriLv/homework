'''a =int(input("Input a:"))
b = int(input("Input b:"))
if a>b:
    print("a>b, a=",a)
else:
    print ("a<b, b=",b)

print("FINISH")'''


b= str('''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''')



b= b.split()
print(b)
c  = ' '.join(b)
up=c.upper()

print("1.")
better = up.count('BETTER')
print("better - ", better, " times")
never = up.count('NEVER')
print("never - ", never, " times")
iss = up.count('IS')
print("is - ", iss, " times")

print("2.")
print(up)

print("3.")
i=c.replace("i","&")
i_count= i.count("&")
print('''"i" replaced - ''', i_count, " times: ", i)



print("-------------------------------------------------------------------------------")

a= input("Input 4 digits number:")

##a="9274"
b= a.split()
one = int(a[0])
two = int(a[1])
three = int(a[2])
four = int(a[3])

print("Your number:", a[0:4])
dobutok = one * two *three *four
print("1.Multiplication =", dobutok)
print("2. Reverse: " ,a[::-1] )
sor = ''.join(sorted(a[:]))
##sor = int(sor)
print("3. Sorted:  ", sor)

print("GOOD JOB !")
