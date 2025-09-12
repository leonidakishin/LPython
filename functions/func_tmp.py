athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]

n= int(input())

def f1(kortej):
    return kortej[0]
def f2(kortej):
    return kortej[1]
def f3(kortej):
    return kortej[2]
def f4(kortej):
    return kortej[3]

g = [f1,f2,f3,f4]
athletes = sorted(athletes,key=g[n-1])
for e in athletes:
    print(*e)