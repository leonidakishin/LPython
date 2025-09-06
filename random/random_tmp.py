import random as r

dg = '23456789'
alth_low = 'qwertyuipasdfghjkzxcvbnm'
alth_upp = 'QWERTYUOPASDFGHJKLZXCVBNM'
all_symb = dg + alth_low + alth_upp

n, m = int(input()), int(input())

pwd = ''
i = 0
while i != n:
    for j in range(m):
        pwd += r.choice(all_symb)
    pwd_set = set(pwd)
    dg_set = set(dg)
    alth_low_set = set(alth_low)
    alth_upp_set = set(alth_upp)
    if pwd_set&dg_set != set() and pwd_set&alth_low_set != set() and pwd_set&alth_upp_set != set():
        print(pwd)
        
        i +=1
    pwd = ''







