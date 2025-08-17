#Магическим квадратом порядка nn называется квадратная таблица размера n×nn×n, 
#составленная из всех чисел 1, 2, 3,  …,  n21,2,3, …, n2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны между собой. 
#Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.


n = int(input())

def read_matrix(n_l):
    matrix_local = []
    for i in range(n_l):
        row = [int(i) for i in input().split()]
        matrix_local.append(row)
    return matrix_local
matrix = read_matrix(n)

all_chisla = []
for k in range(1,n*n + 1):
    all_chisla.append(k)

flg_magic_matrix = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] not in all_chisla:
            flg_magic_matrix = False
            break
        else:
            all_chisla.remove(matrix[i][j])

sum_et = sum(matrix[0])

def matrix_trans(matrix_l,n_l):
    for i in range(n_l):
        for j in range(n_l):
            if i < j:
                matrix_l[i][j], matrix_l[j][i] = matrix_l[j][i],matrix_l[i][j]
    return matrix_l
 


for i in range(n):
    if sum(matrix[i]) != sum_et:
        flg_magic_matrix = False
        break

matrix_t = matrix_trans(matrix, n)  

for i in range(n):
    if sum(matrix[i]) != sum_et:
        flg_magic_matrix = False
        break

sum_main_diag = 0
sum_side_diag = 0
for i in range(n):
    for j in range(n):
        if i == j:
            sum_main_diag += matrix[i][j]
        if j == n - i - 1:
            sum_side_diag += matrix[i][j]  
if sum_main_diag != sum_et or sum_side_diag != sum_et:
    flg_magic_matrix = False

if flg_magic_matrix:
    print('YES')
else:
    print('NO')    
