class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        self.age += 1
        return "Happy Birthday! 🎉🎂"


person1 = Person(name="Ivan", age=15)
print(person1.celebrate_birthday())
print(f"{person1.name} is {person1.age} years old now.")
