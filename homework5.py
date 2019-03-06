print("1. --------------------------------------------------------------------")

'''Program the function distance(p1, p2) which returns the distance between the points p1 and p2 in n-dimensional space. p1 and p2 will be given as arrays.

Your program should work for all lengths of arrays, and should return -1 if the arrays aren't of the same length or if both arrays are empty sets.'''

# x1=4
# x2=6
# y1=5
# y2=6
# p1=[x1,y1]
# p2=[x2,y2]
#
# dist = float(((x1-x2)**2+(y1-y2)**2)**0.5)
#
# print(p1)
# print(dist)

# print('Version 2')
# n=int(input('Input n, n - demensional:'))
# n=3
# p1=[]
# p2=[]
# dist=[]
# for i in range(n):
#     i=input('Input array for p1: ')
#     p1.append(i)
#
# for i in range(n):
#     i=input('Input array for p2: ')
#     p2.append(i)
# print('p1=',p1, ' p2=', p2)
#
# dist=[int(p1[i])+int(p2[i]) for i in range(n)]
# print('dist='dist)
#


print("2. --------------------------------------------------------------------")
'''The Game:
In this game, there are 21 sticks lying in a pile. Players take turns taking 1, 2, or 3 sticks. The last person to take a stick wins. Like this:
Your task:
Create a robot that will always win the game. Your robot will always go first. The function should take an integer and returns 1, 2, or 3.
Example:
make_move(2) == 2
# => 1'''
#
# bot=1
# st=bot
# print('bot choose stick', bot)
# for i in range(bot,22):
#     i= int(input('take your stick 1,2 or 3: '))
#     st=st+i
#     if 21-st<=3:
#         break
# bot = 21- st
# print("bot takes sticks", bot, ' ,bot WIN!!!')



print("3. --------------------------------------------------------------------")
'''Write a function taking in a string like WOW this is REALLY amazing and returning Wow this is really amazing. String should be capitalized and properly spaced. Using re and string is not allowed.
Examples:
filter_words('HELLO CAN YOU HEAR ME') #=> Hello can you hear me
filter_words('now THIS is REALLY interesting') #=> Now this is really interesting
filter_words('THAT was EXTRAORDINARY!') #=> That was extraordinary!'''

# s1=('HELLO CAN YOU HEAR ME')
# s2=('now THIS is REALLY interesting')
# s3=('THAT was EXTRAORDINARY!')
# s=s3
#
# a=s.lower()
# b=s.upper()
# s=b[0]+a[1:]
#
# print(s)



print("4. --------------------------------------------------------------------")
''' Unfinished Loop - Bug Fixing #1
Oh no, Timmy's created an infinite loop! Help Timmy find and fix the bug in his unfinished For Loop!
def create_array(n):
    res=[]
    i=1
    while i<=n: res+=[i]
    return res'''
# n=10
# res=[]
# i=1
# while i<=n:
#     res+=[i]
#     i=i+1
# print(res)
#
# print('need to add   i+=1')