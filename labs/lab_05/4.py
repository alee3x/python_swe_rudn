# Реализуйте программу, которая читает файл с числами и записывает только четные числа в новый файл.
with open("input/numbers_in.txt", "r") as num_in, open(
    "output/numbers_out.txt", "w"
) as num_out:
    for number in num_in:
        if int(number) % 2 == 0:
            print(str(number), file=num_out)
