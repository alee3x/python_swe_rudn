my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]

my_list_1 = set(my_list_1)
my_list_2 = set(my_list_2)

print(list(my_list_1.difference(my_list_2)))

# for iterator in my_list_1:
#     if iterator in my_list_2:
#         print("iter:", iterator)
#         my_list_1.pop(my_list_1.index(iterator))
# print(my_list_1)
