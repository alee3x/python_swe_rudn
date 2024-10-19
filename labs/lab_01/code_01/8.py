# Количество дней занятий
x = int(input("Введите результат в первый день: "))
y = int(input("Введите целевой результат: "))
iterator = 1
while x < y:
    x = x * 1.1
    iterator += 1
print(f"Потребуется {iterator} дней")
