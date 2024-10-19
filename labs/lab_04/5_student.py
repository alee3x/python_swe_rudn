class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        if self.grade >= 60:
            return True
        else:
            return False


student1 = Student(name="John", grade=60)
student2 = Student(name="Bob", grade=50)

print(student1.is_passing())
print(student2.is_passing())
