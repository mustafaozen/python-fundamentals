'''
This script exemplifies basic use of try/except statements to catch errors.
For more details:
https://docs.python.org/3/tutorial/errors.html
'''

# Suppose that we want user to enter an integer. If the user enters a letter, then we will get an error message:
# ValueError: invalid literal for int() with base 10:

# Uncomment the following line and see the error message by entering a letter:
# userInput = int(input('Please enter an integer: '))


# Thanks to try/except statements, we can catch and utilize the errors:
print('Example 1\n')
try:
    userInput = int(input('Please enter an integer: '))
    print('The square of the number is: ', userInput ** 2)
except:
    print('You did not enter an integer! Please try again!')


# There are multiple built-in exception errors in python such as:

# SyntaxError
# RuntimeError
# ValueError
# FileNotFoundError
# ZeroDivisionError
# KeyboardInterrupt
# and so on..

# If we expect multiple errors in a code segment, we can use the error names next to 'except' command and specify the action if it occurs:
print('\nExample 2\n')
try:
    userInput = int(input('Please enter an integer: '))
    print('The number/0 is: ', userInput/0)
except ValueError: # If user do not enter an integer
    print('You did not enter an integer! Please try again!')
except ZeroDivisionError: # If user enters an integer, then we will get an error due to diving it to 0
    print('No, No! You are dividing the number by 0!')

# There is also 'raise' statement which allows the programmer to force an exception error whenever needed:
print('\nExample 3\n')

try:
    num1 = int(input('Please enter an integer: '))
    num2 = int(input('Please enter an integer: '))
    if num2 == 0:
        raise KeyboardInterrupt # Although it is not relevant, I can raise a KeyboardInterrupt exception error because I want!

    print('The num1/num2 is: ', num1/num2)
except ValueError: # If user do not enter an integer
    print('You did not enter an integer! Please try again!')


# It is even possible to create your own exception errors. For details please see: https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions