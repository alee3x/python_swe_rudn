a = int(input())
max = 0
while a > 0:
    i = a % 10
    a = a // 10
    if i > max:
        max = i
print(max)
