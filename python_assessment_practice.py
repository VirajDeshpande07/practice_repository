import threading
from datetime import date
import time
#q1 create a class student with a constructor
class Student():
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = 0   # a private variable inside the current object assigning it value 90.
        self.admission_date = date.today()
        

    
    def get_marks(self):  #q3 getter method
        return self.__marks
    
    def set_marks(self,marks):   #q3 setter method
        if marks<0 or marks>100:
            raise ValueError("Marks must be between 0 and 100")
        self.__marks = marks

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

    #thread function for report generation
    def generate_report(self):
        print("\n Generating student report..")
        time.sleep(3)
        print("\nStudent report generated successfully.")

    #main program
print("\n ====Student Management System===")

    #object creation
roll_no = int(input("Enter student roll no: "))
name = input("Enter Student Name: ")
s1 = Student(roll_no,name)

#q5 exception handling 
try:
    marks = float(input("Enter Student Marks(0-100): "))
    s1.set_marks(marks)
except ValueError as e:
    print("Invalid Marks: ",e)
   
#display details
s1.display_details()

# create and start thread

t1 = threading.Thread(target = s1.generate_report)
t1.start()
t1.join()
print("Execution Complete")





