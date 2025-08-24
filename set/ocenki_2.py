#Даны оценки по математике трех учеников в 10-балльной шкале. 
#Напишите программу, которая выводит такие оценки, которые встречаются не более, чем у двух учеников.

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

st_nm = (st_n|st_m) - st_s
st_ns = (st_n|st_s) - st_m
st_ms = (st_m|st_s) - st_n

st_itog = st_nm | st_ns | st_ms

print(*sorted(st_itog))