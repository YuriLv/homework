
print("Convert a Number to a String -----------------------------------")
n=6
n=str(n)
print(n)

print('----------------------------------------------------------------')
'''reverse('Hello World') == 'World Hello'
reverse('Hi There.') == 'There. Hi' '''


a= "Hello World"
b = 'Hi There.'
a =a.split()
b=b.split()
a = a[::-1]
b= b[::-1]

a = ' '.join(a)
b= ' '.join(b)

print(a+"\n", b)

print('----------------------------------------------------------------')
'''Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to greet him slightly different. She added a special case to her function, but she made a mistake.
Can you help her?
'''

a= input("Write Your name: ")
if a == "Johny":
    print("Hello my love!!!")
else:
    print("I'm glad to hear you!")

print('----------------------------------------------------------------')

