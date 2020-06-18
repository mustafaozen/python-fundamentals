'''
This script exemplifies basic use of string and associated methods in python.
For more details: https://docs.python.org/3/tutorial/introduction.html#strings
'''

# Strings can be created using " or ':

myFistString = 'Hi there!'

str2 = "This is the second string!"

print(myFistString, '\n')
print(str2,'\n')

## Some built-in string methods: ##

# .lower(str): converts whole string to lower case.
str3 = 'UPPER'
print(str3.lower(),'\n')

# .upper(str): converts whole string to upper case.
str4 = 'lower'
print(str4.upper(), '\n')

# .isupper(str): checks if the sting is upper case. The output is boolean.
print(str3.isupper(),'\n')

# len(str): retuns the length of the string. Counts each character of the string including the spaces.
str5 = 'Hello Human'
print(len(str5),'\n')

# The characters of a string are indexed from left to right by starting from 0 to N-1. To pick a specific character of a string:
print('The 5th letter of str5 is: ', str5[4], '\n')

# .index(char); returns the index of a character in a string.
print("The index of 'o' in str5 is: ", str5.index('o'), '\n') # if there were multiple 'o's, then it would return the index of the first one from the left.

# .replace(str): replaces a string with a given input string.
print(str5.replace('Human','World'),'\n')

# int(str): Can convert a string to an integer.
str6 = '824'
number = int(str6)
print('The converted number is: ', number, '\n')

# .split(str): converts a string to a list. By default, it splits based on the spaces.
str7 = "Let's split this string"
print('The default list of str7 is: ', str7.split(), '\n')
print('The custom list of str7 is: ', str7.split("'"), '\n')
print('Another custom list of str7 is: ', str7.split('t'), '\n')