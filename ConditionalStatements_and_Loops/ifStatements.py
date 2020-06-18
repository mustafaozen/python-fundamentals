'''
This script exemplifies basic use of conditional statements in python.
For more details:
https://docs.python.org/3/tutorial/controlflow.html#if-statements
'''

# If statement is a conditional statement which performs a command if a condition is satisfied.
# It has the following general form:
print('The first example:')
condition = True
if condition == True:
    # run this command
    print('Condition is true!')
else:
    # run this command
    print('Condition is false!')

# Actually no need to type "== True" if the variable under control is boolean!
print('\n The second example:')

condition = False
if condition:
    # run this command
    print('Condition is true!')
else:
    # run this command
    print('Condition is false!')

# Multiple conditions can be checked using "elif"
print('\n The third example:')
num = 5
if num < 0:
    print('The number is negative!')
elif num == 0:
    print('The number is zero!')
else:
    print('The number is positive!')