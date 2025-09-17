def ip_10(ip):
    lst_ip = [int(i) for i in ip.split('.')]
    return lst_ip[0]*256**3 + lst_ip[1]*256**2+lst_ip[2]*256+lst_ip[3]

n = int(input())
lst = []
lst = [input() for i in range(n) ]
lst = sorted(lst)
print(*sorted(lst,key=ip_10))
