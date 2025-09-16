summa = int(input())
procenty = 0.15
days = 365

summa_mes = summa + summa*(0.165)
summa_den = summa

for i in range(days):
    itog = summa_den*(procenty/365)
    summa_den += itog
    print(summa_den)

print('Сумма с процентами при ежедневном подсчете: ',summa_den)
print('Сумма с процентами при ежемесячном подсчете: ',summa_mes)
print('Разница: ',summa_den - summa_mes)
