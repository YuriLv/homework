print('''1. ----------------------------------------------------''')
'''Is the string uppercase?
Task
Create a method is_uppercase() to see whether the string is ALL CAPS. For example:
is_uppercase("c") == False
is_uppercase("C") == True
is_uppercase("hello I AM DONALD") == False
is_uppercase("HELLO I AM DONALD") == True
is_uppercase("ACSKLDFJSgSKLDFJSKLDFJ") == False
is_uppercase("ACSKLDFJSGSKLDFJSKLDFJ") == True'''


def is_uppercase(text):

    if text.isupper():
        res = True

    else:
        res = False

    return res

text= "ACSKLDFJSgSKLDFJSKLDFJ"
print("is_uppercase"+ "("+ text + ")" + " == ", is_uppercase(text))

text= "hello I AM DONALD"
print("is_uppercase"+ "("+ text + ")" + " == ", is_uppercase(text))

text= "HELLO I AM DONALD"
print("is_uppercase"+ "("+ text + ")" + " == ", is_uppercase(text))
text = "ACSKLDFJSQSKLDFJSKLDFJ"
print("is_uppercase"+ "("+ text + ")" + " == ", is_uppercase(text))

# text= input("Input text:")
# print("is_uppercase"+ "("+ text + ")" + " == ", is_uppercase(text))


print('''2. ----------------------------------------------------''')
'''HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order!
 Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.
The sorting should NOT be case sensitive
'''
print("Java????  Not clear what should to do")
a=[]
a.sort()
print(a)



print('''3. ---------------------------------------------------- ''')
'''You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was made:
Weekday Month Day, time e.g., Friday May 2, 7pm
You're running out of screen real estate, and on some pages you want to display a shorter format, Weekday Month Day that omits the time.
Write a function, shortenToDate, that takes the Website date/time in its original string format, and returns the shortened format.
Assume shortenToDate's input will always be a string, e.g. "Friday May 2, 7pm". Assume shortenToDate's output will be the shortened string, e.g., "Friday May 2".
'''




def day(d):
    i = d.index(",")
    print(d[0:i])

d = "Friday May 2, 7pm"
day(d)


#
# i=0
# while i<len(date):
#
#     if date[i] == ",":
#         print(date[0:i])
#         break
#     i=i+1
#
# for i in range(len(date)):
#     if date[i] ==",":
#         print(date[0:i])
#         break
#
# i= date.index(",")
# print(date[0:i])
