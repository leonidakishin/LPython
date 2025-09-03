n_strok = int(input())


dct = {}
for i in range(n_strok):
    lst = input().split()
    
    if lst[0] in dct.keys():
        dct[lst[0]] += lst[1] +' '+ lst[2] + '&'
    else:
        dct[lst[0]] = lst[1] +' '+ lst[2] + '&'
    lst.clear()

for k,v in dct.items():
    dct[k] = v.rstrip('&')


for k,v in sorted(dct.items()):
    print(k+':')
    v_sort = v.split('&')
    v_sort.sort()
    print(*v_sort,sep='\n')


                
    
