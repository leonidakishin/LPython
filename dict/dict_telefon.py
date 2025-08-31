# Тимур записал телефоны всех своих друзей, чтобы автоматизировать поиск нужного номера.

# У каждого из друзей Тимура может быть один или более телефонных номеров. Напишите программу,
# которая поможет Тимуру находить все номера определённого друга.
n = int(input())
dct = {}
for _ in range(n):
    v, k = input().lower().split()
    dct[k] = dct.get(k, "") + " " + v
print(dct)
m = int(input())

for _ in range(m):
    abonent = input().lower()
    if dct.get(abonent) == None:
        print("абонент не найден")
    else:
        print(dct[abonent].strip())
