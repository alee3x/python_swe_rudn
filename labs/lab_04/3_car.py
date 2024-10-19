class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"Made by: {self.make}, Model: {self.model}"


car1 = Car(make="Ford", model="F150")

print(car1.describe())
