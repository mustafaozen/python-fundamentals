'''
This script is created as a master class to exemplify use of Interitance in python.

For more details go to: inheritance.py
'''

class Student:

    def __init__(self, name, surname, age, major, gpa):

        self.name = name
        self.surname = surname
        self.age = age
        self.major = major
        self.gpa = gpa

    def checkGPADesignation(self, gpa):

        if (gpa >= 3.5) & (gpa < 3.75):
            print('Cum Laude!')
        elif (gpa >= 3.75) & (gpa < 4.00):
            print('Magna Cum Laude!')
        elif (gpa == 4.00):
            print('Summa Cum Laude!')
        elif (gpa >= 3.00) & (gpa < 3.5):
            print('Honor Student!')
        else:
            print('No designation!')


    def getStudentName(self):
        return self.name

    def setStudentGPA(self,new_gpa):
        self.gpa = new_gpa