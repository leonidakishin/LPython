# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m,
# заполнив ее "диагоналями" в соответствии с образцом.

n, m = [int(i) for i in input().split()]

for i in range(n):
    matrix = [[0] * m for _ in range(n)]


cnt = 2
matrix[0][0] = 1
for j in range(1, m):
    i = 0
    k = j
    while k >= 0:
        matrix[i][k] = cnt
        cnt += 1

        k -= 1
        i += 1
        if i == n:
            break

for i in range(1,n):
    j = m - 1 
    k = i
    while k <= n - 1:
        matrix[k][j] = cnt
        cnt += 1        

        k += 1
        if j == 0:
            break   
        j -= 1

for i in range(n):
    for j in range(m):
        str_aij = str(matrix[i][j])
        print(str_aij.rjust(3), end="")
    print()
