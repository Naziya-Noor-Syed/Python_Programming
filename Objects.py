class Student:
    #default constructor
    def __int__(self):
        pass
    #parametarized constructor
    def __init__(self, name, marks):
        self.name=name
        self.marks = marks
        print("Adding new student database..")

s1 = Student("Karan", 97)
print(s1.name, s1.marks)
