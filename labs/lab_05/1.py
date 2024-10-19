# Напишите программу, которая читает текстовый файл и выводит его содержимое на
# экран.

with open("input/example.txt", "r") as file:
    content = file.read()
    print(content)
