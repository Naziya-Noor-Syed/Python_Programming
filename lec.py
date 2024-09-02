class Person:
    def __init__(self, name, country, dob, age):
        self.name = name
        self.country = country
        self.dob = dob
        self.age = age
p1 = Person("Tony", "Canada", "5/8/1956", "69")
print(p1.age)
