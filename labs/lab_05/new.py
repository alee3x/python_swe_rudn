# Напишите программу, которая читает текстовый файл и выводит его содержимое на
# экран.

with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Создайте программу, которая копирует содержимое одного текстового файла в другой.

with open('input/file2.txt', 'r') as file2, open('output/file1.txt','w') as file1:
    file1.write(file2.read())


# Напишите функцию, которая принимает имя файла и возвращает количество строк в этом файле.
iterator = 0
with open('example.txt', 'r') as file:
    for line in file:
        iterator += 1
print(iterator)

# Реализуйте программу, которая читает файл с числами и записывает только четные числа в новый файл.
with open('input/numbers_in.txt', 'r') as num_in, open('output/numbers_out.txt', 'w') as num_out:
    for number in num_in:
        if int(number) % 2 == 0:
            print(str(number), file=num_out, '\n')
N = int(input("How many files? "))

with open('output/multiple_out.txt', 'w+') as out:
    for i in range(1, N + 1):
        mult_file = "input/multiple" + str(i) + ".txt"
        with open(mult_file, "r") as infile:
            out.write(infile.read())

# Создайте программу, которая считывает данные из JSON-файла и выводит их в удобочитаемом формате.
import json

with open("input/64KB-min.json", "r") as infile:
    json_data = json.load(infile)
    print(json.dumps(json_data, indent = 4, sort_keys=False))

# Реализуйте скрипт, который читает CSV-файл, обрабатывает данные и сохраняет результаты в новом CSV-файле,
#добавляя колонку с расчетом.
import csv

# hw_200.csv:
# height and weight for 200 individuals Each record includes 3 values: index,
# height (inches), weight (pounds). There is also an initial header line

with open("input/hw_200.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    data = list(reader)
    # Calculate Height/Weight Ratio
    data[0].append("\"Height/Weight Ratio (in/lb)\"")
    for i in range(1, len(data)):
        row = data[i]
        ratio = round(((float(row[1]) / float(row[2])) * 100), 2)
        row.append(str(ratio))
        data[i] = row

with open("output/hw_200_modified.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerows(data)
