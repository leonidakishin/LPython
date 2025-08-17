#Дана квадратная матрица чисел. Напишите программу, которая меняет местами элементы, стоящие на главной и побочной диагонали, 
# #при этом каждый элемент должен остаться в том же столбце (то есть в каждом столбце нужно поменять местами элемент на главной 
# #диагонали и на побочной диагонали).


n = int(input())

def read_matrix(n_l):
    matrix_local = []
    for i in range(n_l):
        row = [int(i) for i in input().split()]
        matrix_local.append(row)
    return matrix_local
matrix = read_matrix(n)

def matrix_trans(matrix_l,n_l):
    for i in range(n_l):
        for j in range(n_l):
            if i < j:
                matrix_l[i][j], matrix_l[j][i] = matrix_l[j][i],matrix_l[i][j]
    return matrix_l            


matrix = matrix_trans(matrix,n)

for i in range(n):
    for j in range(n):
        if i == j:
            matrix[i][j],matrix[i][n - 1 - i] = matrix[i][n - 1 - i],matrix[i][j]

matrix = matrix_trans(matrix,n)

for i in range(n):
    print(*matrix[i])