import random as r3
ucheniki_lst = ['Светлана Зуева', 'Аркадий Белых', 'Борис Боков']
#n = int(input())
#ucheniki_lst = [input() for i in range(n)]
n = 3
ucheniki_set = set(ucheniki_lst)

dct_pary = {}

for i in range(n):
    set_i = set()
    set_i.add(ucheniki_lst[i])  
    print(set_i,'set_i')  
    tmp_set = ucheniki_set - set_i
    
    str_tmp_set = ''.join(tmp_set)
    print(str_tmp_set,'tmp')
   
    if len(ucheniki_set) == 2 and str_tmp_set == ucheniki_lst[i]:
        print(ucheniki_set)
        tmp_set = ucheniki_set - tmp_set
    dct_pary[ucheniki_lst[i]] = tmp_set.pop()
    print(dct_pary,'dct')
    ucheniki_set.remove(dct_pary[ucheniki_lst[i]])
    tmp_set.clear()

print(dct_pary)

