n = int(input())
m = int(input())

matrix = []
for i in range(n):
    matrix.append( ['.']*m)

for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            matrix[i][j] = '*'


for i in range(n):
    print(*matrix[i]) 


