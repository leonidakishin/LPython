# На странице каждой задачи онлайн-курсов "Поколения Python" имеется виджет, который отображает общее число учащихся, верно решивших задачу,
# и процент верных решений от общего числа попыток. Напишите программу,
# которая повторяет этот функционал: считает, сколько учеников верно решили задачу, и вычисляет процент верных решений среди всех попыток.
import math
n = int(input())

lst = []

names_set = set()
answers_lst = []

for i in range(n):
    lst.append(input())

lst_tmp = []
set_tmp = set()
correct_ans_unic_cnt = 0
correct_ans_all_cnt = 0
all_ans_cnt = 0
for e_lst in lst:
    lst_tmp = e_lst.split(":")
    if e_lst not in set_tmp: 
        set_tmp.add(e_lst)
        if "Correct" in e_lst:
            correct_ans_unic_cnt += 1
    
    if lst_tmp[0] not in names_set:

            names_set.add(lst_tmp[0])
    if "Correct" in lst_tmp[1]:
        correct_ans_all_cnt += 1
    all_ans_cnt += 1


#print(correct_ans_unic_cnt)
#print(correct_ans_all_cnt)
#print(all_ans_cnt)
if correct_ans_unic_cnt != 0:
    print(f"Верно решили {correct_ans_unic_cnt} учащихся")
    itog = 0
    if (correct_ans_all_cnt/all_ans_cnt*1000)%10 == 5:
        itog = (correct_ans_all_cnt/all_ans_cnt*1000 + 1) / 1000
        print(f'Из всех попыток {int(round(itog*100,2))}% верных')
    elif (correct_ans_all_cnt/all_ans_cnt*1000)%10 > 5:
        print(f'Из всех попыток {int(math.ceil(correct_ans_all_cnt/all_ans_cnt*100))}% верных')         
    else:
        print(f'Из всех попыток {int(math.floor(correct_ans_all_cnt/all_ans_cnt*100))}% верных')
else:
    print("Вы можете стать первым, кто решит эту задачу")
#print(names_set)
