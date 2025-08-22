
#Даны по 10-балльной шкале оценки по информатике трех учеников. 
#Напишите программу, выводящую множество оценок, которые есть и у первого, и у второго учеников, но которых нет у третьего ученика.

n,m,s = input().split(),input().split(), input().split()

#print(n)
def func_1(n_l):
    st_tmp = set()
    for c in n_l:
        st_tmp.add(int(c))
    return st_tmp    


st_n = func_1(n)
st_m = func_1(m)
st_s = func_1(s)

#print(s)

st_it = (st_n&st_m) - st_s  

print(*sorted(st_it,reverse=True))
