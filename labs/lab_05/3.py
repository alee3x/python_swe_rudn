# Напишите функцию, которая принимает имя файла и возвращает количество строк в этом файле.
iterator = 0
with open("input/example.txt", "r") as file:
    for line in file:
        iterator += 1
print(iterator)
