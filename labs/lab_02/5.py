list_size = int(input("Введите размера массива (число N): "))
int_list = []
maximum = -1
print("Введите список чисел:")

for i in range(list_size):
    int_num = int(input())  # input integer

    if int_num > maximum:  # find maximum
        maximum = int_num

    int_list.append(int_num)  # add numbers to the list

print(maximum)

int_list.reverse()
print(int_list)

# start the reals list part
reals_list = []
reals_sum = 0
print("Введите список действительных чисел: \n")

for i in range(list_size):
    real_num = float(input())
    reals_list.append(real_num)
    reals_sum += real_num

reals_arithm_mean = reals_sum / list_size

for zero_check in reals_list:
    zero_index = reals_list.index(zero_check)
    if zero_check == 0.0:
        reals_list[zero_index] = reals_arithm_mean
print(reals_list)
