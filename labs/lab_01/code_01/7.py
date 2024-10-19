# Медицинская анкета
imya = input("Введите ваше имя: ")
familiya = input("Введите вашу фамилию: ")
vozrast = int(input("Введите ваш возраст: "))
ves = int(input("Введите ваш вес: "))

if (vozrast < 30) and (50 <= ves <= 120):
    print("Пациент в хорошем состоянии.")
elif (vozrast > 30) and (vozrast <= 40) and ((ves < 50) or (ves > 120)):
    print("Пациенту следует заняться собой.")
elif (vozrast > 40) and ((ves < 50) or (ves > 120)):
    print("Пациенту нужен врачебный осмотр.")
else:
    print("Я СИГМА КРУТОЙ Я СИГМА СИГМА СИГМА СИГМА")
