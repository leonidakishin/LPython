#На вход программе подаются два числа. Напишите программу, определяющую, есть ли в данных числах одинаковые цифры.

n,m = input(),input()

st_n = set(n)
st_m = set(m)

if st_n.isdisjoint(st_m):
    print('NO')
else:
    print('YES')    

