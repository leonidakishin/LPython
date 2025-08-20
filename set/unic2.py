# Напишите программу для вывода общего количества уникальных символов во всех считанных словах без учета регистра.
n = int(input())
smm = 0
set_smm = set()
for i in range(n):
    string = input()
    string_low = string.lower()
    set_str = set(string_low)
    for e_set in set_str:
        set_smm.add(e_set)


print(len(set_smm))
