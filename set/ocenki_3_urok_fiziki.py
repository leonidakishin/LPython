# Даны по 1010-балльной шкале оценки по физике трех учеников.
# Напишите программу, которая выводит множество оценок третьего ученика, которые не встречаются ни у первого, ни у второго ученика.

n, m, s = input().split(), input().split(), input().split()


# print(n)
def func_1(n_l):
    st_tmp = set()
    for c in n_l:
        st_tmp.add(int(c))
    return st_tmp


st_n = func_1(n)
st_m = func_1(m)
st_s = func_1(s)

st_nm = (st_n | st_m) - st_s
st_ns = (st_n | st_s) - st_m
st_ms = (st_m | st_s) - st_n

st_itog = st_s - st_n - st_m

print(*sorted(st_itog))
