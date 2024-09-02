class Student():
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(self.name, self.id)

s1= Student("Rohan",90)
s1.showdetails()