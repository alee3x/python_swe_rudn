import random

with open("numbers_in.txt", "w") as numbers:
    for i in range(10000):
        print(str(random.randint(1, 1000000)), file=numbers)
