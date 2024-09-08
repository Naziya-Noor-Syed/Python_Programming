class Car():

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("Car stoped..")

class ToyatoCar(Car):
    def __init__(self, name):
        self.name = name

class Mercedes(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyatoCar("yato")
car2 = Mercedes("benz")
print(car1.name)
print(car1.start())

print(car2.name)
print(car2.stop())
