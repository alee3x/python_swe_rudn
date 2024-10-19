class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        return f"{self.name}, says Meow!"


cat1 = Cat(name="Buddy", color="Black")
print(cat1.meow())
