a = [[1,0],[4,1]]
b = [[1,0],[4,1]]
sum_matrix = [[1,0],[4,1]]

def lst_x_lst(lst_1, lst2):
    itog = 0
    for i in range(len(lst_1)):
        itog += lst_1[i]*lst2[i]
    return itog

def matrix_x_matrix(a_l,b_l):
    stolp = []
    sum_matrix_l = [[0,0],[0,0]]
    for k in range(2):    
        for j in range(2):
            for i in range(2):
                stolp.append(b_l[i][j])
                #print(stolp)
            #print('AK',a[k])    
            sum_matrix_l[k][j] = lst_x_lst(a_l[k],stolp)
            stolp.clear()
    return sum_matrix_l

for i in range(24):
    sum_matrix = list(matrix_x_matrix(a,sum_matrix))


for i in range(2):
    for j in range(2):
        str_aij = str(sum_matrix[i][j])
        print(str_aij.rjust(3), end="")
    print()