n,m = [int(i) for i in input().split()]

matrix_n = []
matrix_m = []
matrix_sum = []
for i in range(n):
    lst_chisel = [int(j) for j in input().split()]
    matrix_n.append(lst_chisel)



input()

for i in range(n):
    lst_chisel = [int(j) for j in input().split()]
    matrix_m.append(lst_chisel)

for i in range(n):
    lst_chisel = [0]*m
    matrix_sum.append(lst_chisel)

for i in range(n):
    for j in range(m):
        matrix_sum[i][j] = matrix_n[i][j] + matrix_m[i][j]




for i in range(n):
    for j in range(m):
        str_aij = str(matrix_sum[i][j])
        print(str_aij.rjust(3), end="")
    print()