n = int(input())
k = int(input())

lst = [i for i in range(1,n+1)]

def remove_all_k(lst,k):
    tmp_lst = []
    for i in range(len(lst)):
        if i + 1 <= (len(lst)//k) * k:
            if (i + 1) % k != 0:
                tmp_lst.append(lst[i])
        else:
            tmp_lst = lst[i:] + tmp_lst
            break
    return tmp_lst


# k > len(lst)
def remove_k(lst,k):
    cnt = k // len(lst) + 1
    tmp_lst = lst * cnt
    k_elem = tmp_lst[k - 1]
    k_index = lst.index(k_elem)
    tmp_lst1 = lst[k_index + 1:] + lst[:k_index]
    return tmp_lst1

lst2 = lst

if k == 1 and len(lst) == 2:
    lst2 = lst[1]
else:
    while len(lst2) >= k:
        lst2 = remove_all_k(lst2, k)


    while len(lst2) > 1:
        lst2 = remove_k(lst2,k)

for e in lst2:
    print(e,end=' ')

