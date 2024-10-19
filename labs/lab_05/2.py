# Создайте программу, которая копирует содержимое одного текстового файла в другой.

with open("input/file2.txt", "r") as file2, open("output/file1.txt", "w") as file1:
    file1.write(file2.read())
