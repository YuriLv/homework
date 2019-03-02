print("1. -------------------------------------------------------")
'''You were camping with your friends far away from home, but when it's time to go back, you realize that you fuel is running out
and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.'''

dist=int(input("What is the distance to the nearest pump station?: "))
#dist = 50
run = 25
fuel = 2
if run * fuel >= dist:
    print(True)
else:
    print(False)


print("2. -------------------------------------------------------")
'''You have to write a function that accepts three parameters:

    cap is the amount of people the bus can hold excluding the driver.
    on is the number of people on the bus.
    wait is the number of people waiting to get on to the bus.

If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.'''


cap=int(input("Amount of people the bus can hold excluding the driver: "))
on=int(input("Number of people on the bus: "))
wait= int(input("Number of people waiting to get on to the bus: "))

if  on+wait < cap:
    print("Can pick up all")

elif on>cap:
    print("Error input data!!! Try again")

elif on+wait > cap:
    print("Can pick up", cap-on, "and", on +wait-cap, "are left")
else:
    print("No free space, sorry")

print("3. -------------------------------------------------------")
''' Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
'''
print("Are you playing banjo?")
name = input("Write your name: ")

if name[0] == 'r' or name[0] == 'R':
    print(name+" plays banjo")

else:
    print(name+" does not plays banjo")

print("4. -------------------------------------------------------")

'''Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.'''

a=True
a=str(a)
a=a.replace("True","Yes")
print(a)

b=False
b=str(b)
b=b.replace("False","No")
print(b)


print("5. -------------------------------------------------------")
'''Consider an array of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).'''

a=[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

b=0
for i in a:
    if i == True:
        b=b+1
print(b)

print("6. -------------------------------------------------------")

def correct_tail(body, tail):
    sub = body[len(body)-len(tail)]
    if sub == tail:
         True
    else:
         False