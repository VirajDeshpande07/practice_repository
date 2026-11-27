class Student:
    def __init__(self,roll_no,name):
        self.roll_no = roll_no       #created a class Student with constructor.
        self.name = name
        self.__marks = 90    #private variable of marks with value 90 inside self(current object)

    def get_marks(self):
        return self.__marks
 
s1 = Student(46,"Viraj")   #s1 is the object created of the class student with attributes in it(46,"Viraj").
print(s1.roll_no)
print(s1.name)
print(s1.get_marks())