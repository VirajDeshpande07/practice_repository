from datetime import date
import time
#q1 create a class student with a constructor
class Student():
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.admission_date = date.today()
        self.__marks = 85   # a private variable inside the current object assigning it value 90.

    def set_marks(self,marks):   #q3 setter method
        if marks<0 or marks>100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = marks

    def get_marks(self):  #q3 getter method
        return self.__marks

    #q4 calculate grade
    def calculate_grade(self):
        if self.__marks>=90:
            return "A"
        elif self.__marks>=75:
            return "B"
        elif self.__marks>=60:
            return "C"
        elif self.__marks>=50:
            return "D"
        else:
            return "Fail"
    #q2 and q6 display details
    def display_details(self):
        print("\n ==Student Details==")
        print("Roll No: ",self.roll_no)
        print("Name: ",self.name)
        print("Marks:",self.get_marks())
        print("Grade: ",self.calculate_grade())
        print("Admission Date:",self.admission_date)

    #main program
    print("\n ====Student Management System===")



