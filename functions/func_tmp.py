n = int(input())
lst_global = []
lst2 = []
for i in range(n):
    k = int(input())
    for j in range(k):
        lst = [j for j in input().split()]
        lst2.append(lst[1]) 
    lst_global.append(list(lst2))
    lst2.clear()

if all(map(lambda x: True if '5' in x else False,lst_global)):
    print('YES')
else:
    print('NO')