# Напишите программу для вывода количества уникальных символов каждого считанного слова без учета регистра.
n = int(input())

for i in range(n):
    string = input()
    string_low = string.lower()
    set_str = set(string_low)
    print(len(set_str))
    set_str.clear()
