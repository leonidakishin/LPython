


n = int(input())
dct = {}
for _ in range(n):
    v, k = input().split()
    dct[k] = dct.get(k,'') + " " + v

m = int(input())

for _ in range(m):
    abonent = input()
    if dct.get(abonent) == None:
        print('абонент не найден')
    else:
        print(dct[abonent])      


   