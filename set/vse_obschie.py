# На вход программе подаются натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке.
# Напишите программу, которая выводит все общие цифры в порядке возрастания у всех введенных чисел.

n = int(input())

lst = []

for i in range(n):
    lst.append(input())

lst2 = []
for e_lst in lst:
    lst2.append(set(e_lst))

st = set()
for e_lst2 in lst2:
    if st == set():
        st.update(e_lst2)
    else:
        st.intersection_update(e_lst2)

lst3 = list(st)
for i in range(len(lst3)):
    lst3[i] = int(lst3[i])

print(*sorted(lst3))
