# Создайте программу, которая считывает данные из JSON-файла и выводит их в удобочитаемом формате.
import json

with open("input/64KB-min.json", "r") as infile:
    json_data = json.load(infile)
    print(json.dumps(json_data, indent=4, sort_keys=False))
