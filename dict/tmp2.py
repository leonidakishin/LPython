#Руслан Пирог 1
#Тимур Карандаш 5
#Руслан Линейка 2
#Тимур Тетрадь 12
#Руслан Пирог 3

n = int(input())


dct = {}
for i in range(n):
    lst = input().split()
    if lst[0] not in dct.keys():
        dct[lst[0]] = {lst[1]: int(lst[2])}
    else:
        if lst[1] not in dct[lst[0]].keys():
            dct[lst[0]][lst[1]] = int(lst[2])

        else:

            dct[lst[0]][lst[1]] =  dct[lst[0]].get(lst[1],0) + int(lst[2])
    lst.clear()           



for k, v in sorted(dct.items()):
    print(k+':')
    for k1,v1 in sorted(v.items()):
        print(k1,v1)
