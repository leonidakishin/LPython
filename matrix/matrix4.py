#Напишите программу, которая проверяет симметричность квадратной матрицы относительно главной диагонали.

n = int(input())

def read_matrix(n_l):
    matrix_local = []
    for i in range(n_l):
        row = [int(i) for i in input().split()]
        matrix_local.append(row)
    return matrix_local
matrix = read_matrix(n)


flg_matrix_simetrichna = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            flg_matrix_simetrichna = False
            break
            


if flg_matrix_simetrichna:
    print('YES')
else:
    print('NO')    