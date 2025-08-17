n,m = [int(i) for i in input().split()]

matrix_nm = []
matrix_mk = []
matrix_mlt = []
for i in range(n):
    lst_chisel = [int(j) for j in input().split()]
    matrix_nm.append(lst_chisel)



input()
m,k = [int(i) for i in input().split()]
for i in range(m):
    lst_chisel = [int(j) for j in input().split()]
    matrix_mk.append(lst_chisel)

def lst_x_lst(lst_1, lst2):
    itog = 0
    for i in range(len(lst_1)):
        itog += lst_1[i]*lst2[i]
    return itog

def matrix_x_matrix(matrix_nm_l,matrix_mk_l):
    stolp = []
    
    matrix_mlt_l = []
    for i in range(n):
        lst_chisel = [0]*len(matrix_mk_l[0])
        matrix_mlt_l.append(lst_chisel)

    for p in range(n):    
        for j in range(k):
            for i in range(m):
                stolp.append(matrix_mk_l[i][j])
                #print(stolp)
            #print('AK',a[k])    
            matrix_mlt_l[p][j] = lst_x_lst(matrix_nm_l[p],stolp)
            stolp.clear()
    return matrix_mlt_l




for i in range(n):
    for j in range(k):
        str_aij = str(matrix_x_matrix(matrix_nm, matrix_mk)[i][j])
        print(str_aij.rjust(3), end="")
    print()