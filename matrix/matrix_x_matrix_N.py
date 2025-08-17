n = int(input())

matrix_nm = []

for i in range(n):
    lst_chisel = [int(j) for j in input().split()]
    matrix_nm.append(lst_chisel)

times = int(input()) 


matrix_mlt = matrix_nm.copy()

def lst_x_lst(lst_1, lst2):
    itog = 0
    for i in range(len(lst_1)):
        itog += lst_1[i]*lst2[i]
    return itog

def matrix_x_matrix(a_l,b_l):
    stolp = []
    sum_matrix_l = []
    razmer = len(a_l[0])
    for i in range(razmer):
        lst_chisel_l = [0]*razmer
        sum_matrix_l.append(lst_chisel_l)
    for k in range(razmer):    
        for j in range(razmer):
            for i in range(razmer):
                stolp.append(b_l[i][j])
                #print(stolp)
            #print('AK',a[k])    
            sum_matrix_l[k][j] = lst_x_lst(a_l[k],stolp)
            stolp.clear()
    return sum_matrix_l

for i in range(times - 1):
    matrix_mlt = list(matrix_x_matrix(matrix_nm,matrix_mlt))


for i in range(n):
    for j in range(n):
        str_aij = str(matrix_mlt[i][j])
        print(str_aij.rjust(3), end="")
    print()