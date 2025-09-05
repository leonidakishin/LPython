    import random as r3
    #ucheniki_lst = ['Светлана Зуева', 'Аркадий Белых', 'Борис Боков']
    n = int(input())
    ucheniki_lst = [input() for i in range(n)]
    n = 3
    ucheniki_set = set(ucheniki_lst)

    dct_pary = {}

    for i in range(n-2):
        set_i = set()
        set_i.add(ucheniki_lst[i])  
    
        tmp_set = ucheniki_set - set_i
        dct_pary[ucheniki_lst[i]] = tmp_set.pop()
        ucheniki_set.remove(dct_pary[ucheniki_lst[i]])
        tmp_set.clear()

    print(ucheniki_set,'ucheniki_seti') 

    uchenik_tmp1 = ucheniki_set.pop()
    print(ucheniki_set,'ucheniki_set') 
    uchenik_tmp2 = ucheniki_set.pop()
    if ucheniki_lst[-2] !=  uchenik_tmp1 and ucheniki_lst[-1] !=  uchenik_tmp2:
        dct_pary[ucheniki_lst[-2]] = uchenik_tmp1
        dct_pary[ucheniki_lst[-1]] = uchenik_tmp2
    elif ucheniki_lst[-2] ==  uchenik_tmp1 or ucheniki_lst[-1] ==  uchenik_tmp2:
        dct_pary[ucheniki_lst[-2]] = uchenik_tmp2
        dct_pary[ucheniki_lst[-1]] = uchenik_tmp1   



    print(dct_pary)

