'''
This script exemplifies how to read data from files in python.
For more details:
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
'''

# To write data to a file we first need to open a new file or existing file using 'open()' command in 'w' or 'a' mode.
# 'w' mode will overwrite the file in each run while 'a' mode will append the new data to the end of the file.

# Lets create a new file:
file = open('NewData.txt','w')

file.write('This is the first line of the new file!')

# Lets write a list into the fle:
list = ['Data1', 'Data2', 'Data3']
for l in list:
    file.write('\n'+l)

# After we are done, the file needs to be closed:
file.close()

