s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'
#lst = [c for c in s.split()]
result = {}
#for e in lst:
  #  k, v = e.split(':')
  #  result[int(k)] = v

result = {int(k): v for k, v in [e.split(':') for e in [c for c in s.split()]]}

print(result)



numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]



#for j in numbers:
#    k, v = j , [i for i in range(1,j) if j % i == 0 ]
#    result[k] = v


result = {j: [i for i in range(1,j+1) if j % i == 0 ] for j in numbers }

print(result)