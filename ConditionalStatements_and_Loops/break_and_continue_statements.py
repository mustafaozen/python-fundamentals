'''
This script exemplifies basic use of break and continue statements in python.
For more details:
https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
'''

# "break" statement: It breaks the innermost for or while loop.
print("break statement: \n")
for i in range(2):
    for j in ['A', 'B', 'c', 'D', 'e']:
        print(j,'\n')
        if j.islower():
            print(j,' is a lower case letter! go back.. \n')
            break

print("continue statement: \n")
# "continue" statement: whenever it appears, it continues to the next iteration of the same loop.
for i in range(2):
    for j in ['A', 'B', 'c', 'D', 'e']:
        print(j,'\n')
        if j.islower():
            print(j,' is a lower case letter! keep going.. \n')
            continue