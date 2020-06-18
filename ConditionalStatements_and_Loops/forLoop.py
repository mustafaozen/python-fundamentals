'''
This script exemplifies basic use of for loops in python.
For more details:
https://docs.python.org/3/tutorial/controlflow.html#for-statements
'''

# for loops iterates over the list or sequence of items and performs set of commands underneath.
print('The first example:')
list = ['A', 'B', 1, 2, 'C', 'D']
for item in list:
    print(item)

print('\n The second example:')

# We can also run for loop over a string:
str = 'Python3'
for char in str:
    print(char)

print('\n The third example:')

# for loops using range() function:
for i in range(3): # range(n): creates a range from 0 to n-1
    print(i)

# Nested for loop:
print('\n The fourth example:')
for i in range(2):
    print('outer loop \n')
    for j in range(3):
        print('inner loop \n')