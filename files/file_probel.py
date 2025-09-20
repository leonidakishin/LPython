import string

file_name = "data.txt"

with open(file_name, "r", encoding="utf-8") as file:
    lst = []
    for line in file:
        lst.append(map(lambda x: x if x.isdigit() else " ", line))
summa = 0
for e in lst:
    lst = [int(i) for i in "".join(e).split()]
    summa += sum(lst)

print(summa)
