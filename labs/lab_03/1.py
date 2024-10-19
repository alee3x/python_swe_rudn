#
# zadanie 1
#
def name_age_city(name, age, city):
    s = name + ", " + str(age) + ", " + city
    return s


print(name_age_city("Ivan", 20, "Moscow"))


#
# zadanie 2
#
def maxnum(x, y, z):
    a = max(x, y)
    a = max(a, z)
    return a


a, b, c = map(int, input("Введите числа в строке - a b c = ").split())

print("maxnum(a, b, c)", maxnum(a, b, c))


#
# zadanie 3
#
name = input("Имя игрока: ")

player = {"name": name, "health": 100, "damage": 50}
enemy = {"name": "enemy", "health": 100, "damage": 50}


def attack(attacker, victim):
    victim["health"] = victim["health"] - attacker["damage"]
    return victim


print(attack(enemy, player))


#
# zadanie 4
#
player = {"name": name, "health": 100, "damage": 50, "armor": 1.2}
enemy = {"name": "enemy", "health": 100, "damage": 50, "armor": 1.1}


def armored_damage(attacker, victim):
    damage = attacker["damage"] / victim["armor"]
    return damage


def attack(dmg, victim):
    victim["health"] = int(victim["health"] - dmg)
    return victim


print(attack(armored_damage(enemy, player), player))


#
# zadanie 5
#


#
# 5.1
#
def list_sum(massiv):
    massiv_sum = 0
    for num in massiv:
        massiv_sum += num
    return massiv_sum


def list_mean_arithm(massiv):
    return list_sum(massiv) / len(massiv)


massiv_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
massiv_2 = [93, 64, 0, 50, 86, 39, 43, 52, 85, 95, 62, 54, 60, 47, 762]
massiv_3 = [57, 28, 33, 95, 96, 0, 3, 74, 91, 22, 90, 61, 52, 79, 38]

print(massiv_1, massiv_2, massiv_3, sep="\n")

print(list_sum(massiv_1), list_sum(massiv_2), list_sum(massiv_3), sep="\n")

print(
    list_mean_arithm(massiv_1),
    list_mean_arithm(massiv_2),
    list_mean_arithm(massiv_3),
    sep="\n",
)


#
# 5.2
#
def hypotenuse_max_min(a, b, c, d):
    import math

    h_1 = math.sqrt(a**2 + b**2)
    h_2 = math.sqrt(c**2 + d**2)
    print("max_hyp", max(h_1, h_2))
    print("min_hyp", min(h_1, h_2))


hypotenuse_max_min(3, 4, 12, 5)


#
# 5.3
#
def letters_sort(word):
    # split word into individual letters
    letters = [l for l in word]
    # start sorting (using bubble sort)
    for i in range(len(letters) - 1):
        for j in range(i, len(letters)):
            # letters[index].lower() is lowercasing every letter for correct letter ordering
            # because Python considers 'A' < 'a', 'B' < 'b', etc.
            if letters[j].lower() < letters[i].lower():
                letters[i], letters[j] = letters[j], letters[i]
    # join sorted list back into single word
    word = "".join(letters)
    return word


def paragraph_sort(paragraph):
    delims = {
        ",",
        ".",
        ";",
        ":",
        '"',
        "'",
        "(",
        ")",
        "[",
        "]",
        "-",  # these are
        "—",  # three different
        "–",  # types of dashes
        "!",
        "?",
        "\\",  # backslash must be escaped
        "/",
        " ",
    }
    paragraph = paragraph.split(" ")
    for i in paragraph:
        word = ""
        i_sorted = ""
        for j in i:
            if j not in delims:
                word += j
            else:
                i_sorted += letters_sort(word) + j
                word = ""
                i_sorted += letters_sort(word)
                paragraph[paragraph.index(i)] = i_sorted
    return " ".join(paragraph)


print(
    paragraph_sort(
        "Here\'s to the crazy ones, the misfits, the rebels, the troublemakers,
        the round pegs in the square holes... the ones who see things
        differently - they’re not fond of rules... You can quote them, disagree
        with them, glorify or vilify them, but the only thing you can\'t do is
        ignore them because they change things... they push the human race
        forward, and while some may see them as the crazy ones, we see genius,
        because the ones who are crazy enough to think that they can change the
        world, are the ones who do."
    )
)


#
# zadanie 6
#
def tochka_vnutri(a, b, R, p1, p2):
    import math

    A_to_P = math.sqrt((a - p1) ** 2 + (b - p2) ** 2)
    if A_to_P < R:
        print(f"Точка с координатами ({p1,p2}) лежит внутри окружности")
    else:
        print(f"Точка с координатами ({p1,p2}) не лежит внутри окружности")


R = int(input("Введите радиус окружности: "))

a, b = map(
    int, input("Введите через пробел a, b для (x - a)^2 + (y - b)^2 = R^2: ").split()
)

p1, p2 = map(
    int, input("Введите через пробел координаты p1, p2 точки P(p1, p2): ").split()
)
tochka_vnutri(a, b, R, p1, p2)

f1, f2 = map(
    int, input("Введите через пробел координаты f1, f2 точки F(f1, f2): ").split()
)
tochka_vnutri(a, b, R, f1, f2)

q1, q2 = map(
    int, input("Введите через пробел координаты q1, q2 точки Q(q1, q2): ").split()
)
tochka_vnutri(a, b, R, q1, q2)


#
# 6.2
#
def gcd(a, b):
    a, b = max(a, b), min(a, b)
    while a != 0:
        r = a % b
        if r == 0:
            return b
            break
        else:
            a = b
            b = r


def lcm(a, b):
    return (a * b) / (gcd(a, b))


def rationals_diff(a, b, c, d):
    bd = int(lcm(b, d))
    a = int(a * (bd / b))
    c = int(c * (bd / d))
    ac = a - c
    if ac == 0:
        otvet = 0
    else:
        otvet = str(ac) + "/" + str(bd)
    return otvet


a, b = map(int, input("Введите дробь в формате a/b = ").split("/"))
c, d = map(int, input("Введите дробь в формате c/d = ").split("/"))
print("Difference of rationals =", rationals_diff(a, b, c, d))


#
# 6.3
#


def triangle_square(a, b, c):
    import math

    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S


def tetragon_square(a, b, c, d, l):
    S1 = triangle_square(a, b, l)
    S2 = triangle_square(c, d, l)
    return S1 + S2


a, b, c, d, l = map(
    int,
    input(
        "Введите через пробел длины сторон четырёхугольника a, b, c, d и диагональ l: "
    ).split(),
)

print(tetragon_square(a, b, c, d, l))
