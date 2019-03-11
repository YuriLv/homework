print('1. -----------------------------------------------------')
'''Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.
Example

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
'''
#
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
#
# def array1(a):
#     c=0
#     m=0
#
#     for i in range(len(a)):
#
#         if int(a[i])>0:
#             c=c+1
#         else:
#             m=int(a[i])+m
#     l=[c,m]
#     return l
# print(array1(a))
#

print('2. -----------------------------------------------------')
#
# '''In this kata you will create a function that takes in a list and returns a list with the reverse order.'''
#
# arg=[1,3,5,6,76,3]
#
# def rev(arg):
#
#     arg.reverse()
#     return arg
#
# print(rev(arg))
#
# print(rev([3,1,5,4]))
#

print('3. -----------------------------------------------------')
# '''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#
#     Note: If the number is a multiple of both 3 and 5, only count it once.
# '''
#
# n=int(input("input number:"))
# # n=10
# s=0
# for i in range(n):
#     if i%3==0 or i%5==0:
#         s=s+i
#
# print("total sum is", s)
# 58,64,74,75,69,71,70,65,61,74,85,92,91,84
