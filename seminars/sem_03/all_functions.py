def is_even(x: int):
    if x % 2 == 0:
        return True
    else:
        return False


def factorial(x: int):
    i = 1
    x_fact = 1
    for i in range(1, x + 1):
        x_fact = x_fact * i
    return x_fact


def power(x: int, y: int):
    return x**y


def max_of_three(x: int, y: int, z: int) -> int:
    a = max(x, y)
    a = max(a, z)
    return a


def is_palindrome(s: str):
    n = len(s) - 1
    for i in range((n + 1) // 2):
        if s[i] != s[n - i]:
            return False
            break
    return True


def count_vowels(stroka: str):
    iterator = 0
    glasnie = {
        "а",
        "у",
        "о",
        "и",
        "э",
        "ы",
        "я",
        "ю",
        "е",
        "ё",
        "a",
        "e",
        "i",
        "o",
        "u",
    }
    for i in stroka:
        if i in glasnie:
            iterator += 1
    return iterator


def is_prime(number: int, primes_set: set):
    for divisor in primes_set:
        if (number % divisor == 0) or (number == 1):
            return False
            break
    return True


def find_primes(start: int, finish: int):
    primes_set = {2, 3, 5, 7, 11}
    if start % 2 == 0:
        checking = start + 1
    else:
        checking = start
    while checking <= finish:
        if is_prime(checking, primes_set):
            primes_set.add(checking)
        checking += 2
    return primes_set


# a = int(input("a = "))

# print("is_even(a):", is_even(a))

# print("factorial(a):", factorial(a))

# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))

# print("power(x, y):", power(x, y))

# print("max_of_three(x, y, z):", max_of_three(x, y, z))

# s = input("s = ")
# print("is_palindrome(s: str):", is_palindrome(s))

# vow_str = input("string for vowels = ")
# print("count_vowels(vow_str):", count_vowels(vow_str))

x = int(input("x = "))
y = int(input("y = "))

all_primes = find_primes(x, y)

removing = set()

for i in all_primes:
    if i < x or i > y:
        removing.add(i)

all_primes = all_primes.difference(removing)
print(sorted(all_primes))
# for number in all_primes:
#     palindrom = str(number)
#     if is_palindrome(palindrom):
#         print(number)
