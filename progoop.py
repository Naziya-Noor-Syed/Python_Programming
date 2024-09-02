class Student:

    #default constructor
    def __init__(self):
        pass
    #paramitarized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in the database...")

s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("Arjun", 86 )
print(s2.name, s2.marks)
