# Запрос числа, которое должно попасть в диапазон от
a = 11
while (a >= 10) or (a <= 0):
    a = int(input("Введите число: "))
    if (a >= 10) or (a <= 0):
        print("Введено неверно.")
        print(
            "Число должно быть строго больше нуля и строго меньше десяти. Попробуйте ещё раз."
        )
print("Введено верно, вот ваш ответ:", a**2)
