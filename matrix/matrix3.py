#Напишите программу, которая меняет местами столбцы в матрице.
n = int(input())
m = int(input())
def read_matrix(n_l):
    matrix_local = []
    for i in range(n_l):
        row = [int(i) for i in input().split()]
        matrix_local.append(row)
    return matrix_local
matrix = read_matrix(n)

string = input().split()

j1 = int(string[0])
j2 = int(string[1])


for i in range(n):
    for j in range(m):
        if j == j1:
            matrix[i][j1], matrix[i][j2] = matrix[i][j2], matrix[i][j1]


for i in range(n):
    print(*matrix[i])

