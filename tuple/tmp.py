numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))

lst_sum = []

for i in range(len(numbers)):
    lst_sum.append(sum(numbers[i])/len(numbers[i]))
    
print(lst_sum)   
