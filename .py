import threading
import time
from datetime import date


# Q1: Create Student class with constructor
class Student:
    def __init__(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = 0
        self.admission_date = date.today()

    # Q3: Getter
    def get_marks(self):
        return self.__marks

    # Q3: Setter
    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.__marks = marks

    # Q4: Calculate Grade
    def calculate_grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 60:
            return "C"
        elif self.__marks >= 40:
            return "D"
        else:
            return "Fail"

    # Q2 and Q6: Display student details
    def display_details(self):
        print("\n----- STUDENT DETAILS -----")
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.get_marks())
        print("Grade:", self.calculate_grade())
        print("Admission Date:", self.admission_date)


# Q8: Thread function for report generation
def generate_report():
    print("\nGenerating student report...")
    time.sleep(3)
    print("Student report generated successfully!")


# Main program
print("===== STUDENT MANAGEMENT SYSTEM =====")

# Create object
roll = int(input("Enter Roll Number: "))
name = input("Enter Student Name: ")

student = Student(roll, name)

# Q5: Exception handling
try:
    marks = float(input("Enter Marks (0-100): "))
    student.set_marks(marks)

except ValueError as e:
    print("Invalid Marks:", e)
    print("Setting marks to 0.")
    student.set_marks(0)

# Display details
student.display_details()

# Q8: Create and start thread
t1 = threading.Thread(target=generate_report)

t1.start()

# Wait for thread to finish
t1.join()

print("\nProgram Completed!")