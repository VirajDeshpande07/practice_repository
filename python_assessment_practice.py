class Student():
    def __init__(self,roll_no,name):
        self.roll_no = roll_no
        self.name = name
        self.__marks = 85   # a private variable inside the current object assigning it value 90.

    def set_marks(self,marks):   #setter method
        self.__marks = marks

    def get_marks(self):  #getter method
        return self.__marks

s1 = Student(46,"Viraj")
s1.set_marks(95)
print("Roll Number: ",s1.roll_no)
print("Name: ",s1.name)
print("marks:",s1.get_marks())