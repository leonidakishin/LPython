#На вход программе на первой строке подаются коэффициенты многочлена, разделенные символом пробела и целое число x на второй строке.
#  Напишите программу, которая вычисляет значение указанного многочлена при заданном значении x.
from functools import reduce
lst = [int(i) for i in input().split()]
x = int(input())

def evaluate(coeff, x):

    lst_x = []
    for i in range(len(coeff)):
        lst_x.append(x**(len(coeff) - i - 1))

    lst_tmp = map(lambda x,a: x*a, lst_x, coeff)
    
    print(reduce(lambda x,y: x+y,lst_tmp,0))

evaluate(lst,x)


