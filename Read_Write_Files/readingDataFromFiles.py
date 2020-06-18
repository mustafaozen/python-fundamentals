'''
This script exemplifies how to read data from files in python.
For more details:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
'''

# To open or load a data file we use 'open()' method in which we provide file name with extension and mode.
# Mode can be:
    # 'r': read
    # 'w': write
    # 'r+': read and write
    # 'a' append to the end of the file
    # 'b': opens the file in binary mode

exampleData = open('Data.txt',mode = 'r')

# The built-in attributes to use for read data:

# .readable(): checks if the loaded file is readable (returns Boolean)
if exampleData.readable():
    print('The loaded Data.txt is readable!')
else:
    print('The loaded Data.txt is not readable!')

# .read(): reads all of the information provided in the file
print('\n', exampleData.read())

# .readline(): reads the first line of the file and then increments the cursor. If it is called again then it reads the next line.
# Since we called .read() method above, the cursor currently at the end of the file. There fore we first reset it using .seek() method:
exampleData.seek(0)
print('\nThe first line is: ', exampleData.readline())
print('The second line is: ', exampleData.readline())

# .readlines(): it reads all of the data into a list
exampleData.seek(0)
dataList = exampleData.readlines()
print('\nThe data list is: ', dataList, '\n') # Every line of the file becomes an entry of the list

# We can even run a for loop on every lines of the file:
exampleData.seek(0)
for line in exampleData.readlines():
    print(line)

# Finally we need to close the file after we are done with our operation on it!
exampleData.close()