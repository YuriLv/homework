print('1. -------------------------------------------------------------------------')

'''Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.
For example:
summation(2) -> 3
1 + 2
summation(8) -> 36
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8'''

n=8
# n=int(input("write the number n:"))
s=0
for i in range(n+1):
    s=s+i
print('Total sum of n is:',s)



print('2. -------------------------------------------------------------------------')
'''Your collegue wrote an simple loop to list his favourite animals. But there seems to be a minor mistake in the grammar, which prevents the program to work. Fix it! :)
If you pass the list of your favourite animals to the function, you should get the list of the animals with orderings and newlines added.
For example, passing in:
animals = [ 'dog', 'cat', 'elephant' ]
will result in:
list_animals(animals) == '1. dog\n2. cat\n3. elephant\n'
def list_animals(animals):
    list = ''
    for i in range(animals):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list
'''
animals = [ 'dog', 'cat', 'elephant' ]

def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

print(list_animals(animals))


print('3. -------------------------------------------------------------------------')
'''Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
double_char("String") ==> "SSttrriinngg"
double_char("Hello World") ==> "HHeelllloo  WWoorrlldd"
double_char("1234!_ ") ==> "11223344!!__  "
def double_char(s):
    pass'''

s='String'
tex=s
for i in range(len(s)):
    tex=tex.replace(s[i],s[i]*2)

print(tex)
