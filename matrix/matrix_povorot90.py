n = int(input())

matrix = [input().split() for _ in range(n)]

def matrix_trans(matrix_l,n_l):
    for i in range(n_l):
        for j in range(n_l):
            if i < j:
                matrix_l[i][j], matrix_l[j][i] = matrix_l[j][i],matrix_l[i][j]
    return matrix_l    

matrix_t = matrix_trans(matrix,n)

x = n // 2

for i in range(n):
    for j in range(x):
        matrix_t[i][j], matrix_t[i][n - j - 1] = matrix_t[i][n - j - 1], matrix_t[i][j]

for i in range(n):
    print(*matrix_t[i]) 

