absc = [float(i) for i in input().split()] 
ordi = [float(i) for i in input().split()] 
appl = [float(i) for i in input().split()]


#print(*zip(absc, ordi, appl))
print(*map(lambda x: True if x[0]**2+x[1]**2+x[2]**2 <= 4 else False,zip(absc, ordi, appl)))

print(all(map(lambda x: True if x[0]**2+x[1]**2+x[2]**2 <= 4 else False,zip(absc, ordi, appl))))