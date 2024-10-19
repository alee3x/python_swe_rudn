vremya = int(input("Введите время в секундах: "))
chasov = vremya // 3600
minut = (vremya - (chasov * 3600)) // 60
sekund = vremya - (chasov * 3600) - (minut * 60)
chasov = chasov % 24

print(f"{chasov:0>2}:{minut:0>2}:{sekund:0>2}")
