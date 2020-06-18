'''
This script exemplifies basic use of tuples and dictionaries in python.
For more details:
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
https://docs.python.org/3/tutorial/datastructures.html#dictionaries
'''

## Tuples ##
# tuples are immutable data types:
tup = (1,2)
print('Here is the tuple: ', tup, '\n')

# They are also indexed like lists:
print('The first component of the tuple is: ', tup[0], '\n')

# we can define nested tuples as well:
nestTup = ((1,2,3), (4,5,6))
print('Here is the nested tuple: ', nestTup, '\n')
print('The second component of the second tuple is: ', nestTup[1][1], '\n')

# They cannot be changed because they are immutable.
#tup[0] = 3 # will cause the following error: "'tuple' object does not support item assignment"
#print('The updated tuple is: ', tup, '\n')

## Dictionaries ##

# Dictionaries are a data type which is indexed by keys.
d = {'key1': 'A', 'key2': 'B', 'key3': 'C'}
print('Here is the dictionary: ', d, '\n')

# Any element of a dictionary can be reached using the keys:
e = d['key2']
print('The second entry of the dictionary is: ', e, '\n')

# The keys and entries do not have to be strings or characters, numbers will work too.
d2 = {1: 10, 2: 20, 3: 30}
print('Here is the dictionary with number entries and keys: ', d2, '\n')
print('The second entry of d2 is: ', d2[2], '\n')

# Some built-in attributes for dictionaries:

# .get(key): retrieves the element associated with the key
e3 = d.get('key3')
print('The third entry of the dictionary is: ', e3, '\n')

# .keys(): returns the list of keys of the dictionary
print(d.keys(),'\n')

# .values(): returns the list of values of the dictionary
print(d.values(), '\n')

# .pop(key): returns the element of key and also removes it from the dictionary
l = d.pop('key3')
print('The popped item is: ', l, '\n')
print('The updated dictionary is: ', d, '\n')

# .copy(): copies the dictionary into a new variable
dnew = d.copy()
print('Copy of dictionary d is: ', dnew, '\n')

# .clear(): deletes all of the entries of the dictionary
dnew.clear()
print('The cleared dictionary is: ', dnew, '\n')