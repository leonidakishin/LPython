from decimal import *
num = Decimal(input())

s = str(num)
lst = [int(i) for i in s if i != '.']
   
print(max(lst) + min(lst))    