n, m = [int(i) for i in input().split()]

for i in range(n):
    matrix = [[0] * m for _ in range(n)]

lst_chisel = [i for i in range(1,n*m + 1)]


#print(lst_chisel)
i_start_m = 0
j_start_m = 0
i_end_m = n
j_end_m = m

while len(lst_chisel) != 0:

    i_start = i_start_m
    j_start = j_start_m
    i_end = i_end_m
    j_end = j_end_m

    print(lst_chisel)  
    print()

    print(i_start,j_start,i_end,j_end)
    print()


    for j in range(j_start, j_end):
        if len(lst_chisel) == 0:
            break
        matrix[i_start][j] = lst_chisel.pop(0)
       
    i_start += 1
    j_start, j_end = j_end - 1, j_start

    for i in range(i_start, i_end):
        if len(lst_chisel) == 0:
            break
        matrix[i][j_start] =  lst_chisel.pop(0)
        
    
    j_start -= 1
    i_start, i_end = i_end - 1, i_start

    for j in range(j_start, j_end - 1, -1):
        if len(lst_chisel) == 0:
            break
        matrix[i_start][j] = lst_chisel.pop(0)
        

    i_start -= 1
    

    for i in range(i_start, i_end - 1, -1):
        if len(lst_chisel) == 0:
            break
        matrix[i][j_end] = lst_chisel.pop(0)
        i_start = i    
 

    i_start_m += 1
    j_start_m += 1
    i_end_m -= 1 
    j_end_m -= 1



##########################################################################


##################################################################################


print(lst_chisel)

for i in range(n):
    for j in range(m):
        str_aij = str(matrix[i][j])
        print(str_aij.rjust(3), end="")
    print()