'''
This script exemplifies how to use inheritance.

Inheritance allow us to prevent recoding every functions for each class we define if there is commonality.

For instance, we can create Student class with multiple functions. Then when we want to create a engineeringStudents class
we can use the functions defined in Student class by inheriting these two class. We know that any engineer student is a
Student! In this example, Student class is called as "master class".

Another example is that our master class could be Vehicle class and the subclass could be SUV class. Any SUV is a Vehicle!

For more details:
https://docs.python.org/3/tutorial/classes.html#inheritance
'''

# Lets define an engineeringStudents class which inherits Student class that is defined in classAndObjects.py

# Note that master class do nt have to have __init__() method. You can basically create a class with bunch of functions
# without constructor.

# First import the master class:
from masterClass import Student

# Create the subclass:
class engineeringStudents(Student):

    def __init__(self, name, surname, gpa):
        self.name = name
        self.surname = surname
        self.gpa = gpa

    def department(self):
        print('Electrical and Computer Engineering')


# Now when we create an object from engineeringStudents class, we will be able to reach both engineeringStudents class
# functions and Student class functions.

engObj = engineeringStudents(name = 'Lily', surname = 'McConnor', gpa = 3.15)

# Lets learn the department of this engineering student:

engObj.department()

# Lets also use one of the functions defined in Student class:

name = engObj.getStudentName() # getStudentName is defined in masterClass.py file
print(name, 'is an Electrical and Computer Engineering student!')

engObj.checkGPADesignation(engObj.gpa)