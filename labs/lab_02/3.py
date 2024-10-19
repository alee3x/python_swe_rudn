S = [2, 2, 5, 12, 8, 2, 12]
S_mod = []
for i in S:
    if S.count(i) == 1:
        S_mod.append(i)
print(S_mod)
