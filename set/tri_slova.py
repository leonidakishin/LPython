lst = input().split()

set1 = set(lst[0])
set2 = set(lst[1])
set3 = set(lst[2])

if set1 == set2 == set3:
    print("YES")
else:
    print("NO")
