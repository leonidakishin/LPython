import math as m
n = int(input())
func_name = input()

def квадрат(n):
    return n**2

def корень(n):
    return m.sqrt(n)

def куб(n):
    return n**3

def модуль(n):
    return abs(n)

def синус(n):
    return m.sin(n)

commands = {'квадрат': квадрат,'корень': корень,'куб': куб,'модуль': модуль,'синус': синус}

def dejstvie(n,func):
    return func(n)

print(dejstvie(n,commands[func_name]))