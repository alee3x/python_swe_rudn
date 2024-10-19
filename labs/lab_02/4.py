S = input("Введите строку: ")
S = S.split(" ")
iterator = 0
for slovo in S:
    if slovo[0] == "е" or slovo[0] == "Е":
        iterator += 1
print(iterator)
