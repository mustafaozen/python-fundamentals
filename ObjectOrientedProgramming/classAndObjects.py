'''
This script exemplifies how to create classes and class objects.
For more details:
https://docs.python.org/3/tutorial/classes.html
'''

# Classes are very useful to create in a sense a data type for which we can define many functionality.

# The most typical example would be defining a student class:

class Student:

    def __init__(self, name, surname, age, major, gpa):

        self.name = name
        self.surname = surname
        self.age = age
        self.major = major
        self.gpa = gpa

# Within the class, we can create multiple functions. These functions can be reached by the object that we create
# from this class.

    def checkGPADesignation(self, gpa):

        if (gpa >= 3.5) & (gpa < 3.75):
            print('Cum Laude!')
        elif (gpa >= 3.75) & (gpa < 4.00):
            print('Magna Cum Laude!')
        elif (gpa == 4.00):
            print('Summa Cum Laude!')
        else:
            print('No designation!')


    def getStudentName(self):
        return self.name

    def setStudentGPA(self,new_gpa):
        self.gpa = new_gpa


# Creating a class object:

studentObj1 = Student(name = 'Adam', surname = 'Taylor', age = '20', major = 'ECE', gpa = 3.63)
# The same object can be created without using the variable names:
# studentObj1 = Student('Adam', 'Taylor', '20', 'ECE', 3.63)

'''
Note: If the created class is in another python file, then we need to first import the class in the script we want to use it.
We would type:

from PythonFileName import Student
obj = Student(...) 
'''

# We can use the methods defined in the class using the object we created:
studentName = studentObj1.getStudentName()
print('The name of the student 1 is: ', studentName, '\n')

# The information of student can also be reached using objectName.varName:
studentGPA = studentObj1.gpa
print('The GPA of student 1 is: ', studentGPA, '\n')

# Lets check if we have any honor designation for this GPA:
studentObj1.checkGPADesignation(studentGPA)

# We can also change an object value by using set methods that we can create within the class:
studentObj1.setStudentGPA(3.8)
# Lets check again the honor designation for the updated GPA:
studentObj1.checkGPADesignation(studentObj1.gpa)