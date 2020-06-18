'''
This script exemplifies basic use of lists and associated methods in python.
For more details: https://docs.python.org/3/tutorial/introduction.html#lists
'''

# Lists are widely used data type in python. They can include characters, strings, numbers, etc as their entries.
list1 = ['Name', 'Surname', 5, 2.5, 'A', True]
print('The created list is: ', list1, '\n')

# The list are indexed from left to right starting from 0 to N-1. To retrieve any entry of the list use:
entry = list1[1]
print('The second entry of the list is: ', entry, '\n')

# Multiple entries of the list can be retrieved as follows:
multiEntry = list1[2:4] # Retrieve entries indexed by 2 and 3 (excludes the 4th entry!)
print('The multiEntry is: ', multiEntry, '\n')

# Another example:
multiEntry2 = list1[1:] # Retrieve entries starting index 1 to end
print('The multiEntry2 is: ', multiEntry2, '\n')

## Some useful built-in list attributes: ##

# .extend(list): appends two lists
list2 = ['Second', 'List', 1, 2]
list1.extend(list2)
print('The extended list2 is: ', list1, '\n')

# .append(var): appends the entry var to the end of the list
list2.append('New entry')
print('The updated list2 is: ', list2, '\n')

# .index(var): returns the index of var from the list if it exists
ind = list2.index('Second')
print("The index of 'Second' in list2 is: ", ind, '\n')

# .insert(ind, var): inserts var into the given index ind
list2.insert(2,'A')
print("Inserted 'A' to the list2: ", list2, '\n')

# .remove(var): removes var from the list
list2.remove('New entry')
print("Removed 'New entry' from the list2: ", list2, '\n')

# .count(var): counts the number of var in the list
list2.insert(5,'A')
print('The updated list is: ', list2, '\n')
c = list2.count('A')
print("The number of 'A' in the list2 is: ", c, '\n')

# .sort(): sorts the list in ascending order
list3 = ['D', 'E', 'A', 'C', 'B']
print('The new list3 is: ', list3, '\n')
list3.sort()
print('The sorted list3 is: ', list3, '\n')

# .reverse(): reverses the list order
list3.reverse()
print('The reversed list3 is: ', list3, '\n')

# .pop(): pops(removes) the last entry of the list
lastEntry = list3.pop()
print('The last entry of list3 is: ', lastEntry, '\n')
print('The updated list3 is: ', list3, '\n')

# It is possible to pop any entry by passing the index.
entry1 = list3.pop(1)
print('The entry with index 1 of list3 is: ', entry1, '\n')
print('The updated list3 is: ', list3, '\n')

# .copy(): copies entries of a list to a new variable.
# copiedList = list2 won't exactly copy list2 into copiedList. '=' sign will make them share the same address in the memory.
# If one of them is changed, the other one will also change. Therefore, .cop() is used.
newList = list3.copy()
print('The copied list is: ', newList, '\n')

# .clear(): deletes all of the entries of the list.
newList.clear()
print('The cleared list is: ', newList, '\n')
print('The list3 remains the same due to using .copy while creating the newList!: ', list3, '\n')