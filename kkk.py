from math import *

n = int(input())
if n > 2:
    print(int(ceil(log(n+1,2))))

else:
    print(n)