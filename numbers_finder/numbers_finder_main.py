from random import *
print('Добро пожаловать в числовую угадайку!')
print('Введите верхнюю границу для загадывания:')

max_n = int(input())

n = randint(1,max_n)



#user_input_main = input()

def is_valid(user_input):
    if user_input.isdigit():
        user_input = int(user_input)
        if 1 <= user_input <= 100:
            return True
        else:
            return False
    else:
        return False



cnt = 0

while True:
    if  cnt == 0:
        print(f'Я загадал число от 1 до {max_n}. \nПопробуй угадать, Леонид! \nВведи число от 1 до {max_n}:')
    user_input_main = input()
    if is_valid(user_input_main):
        user_input_main = int(user_input_main)
        if user_input_main > n:
            print('Ваше число больше загаданного, попробуйте еще разок')
            cnt += 1
        if user_input_main < n:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            cnt += 1
        if user_input_main == n:
            cnt += 1
            print('Вы угадали, поздравляем!')
            print('Вы использовали ', cnt, 'попыток.')
            print('Начать заново? \nВведите "да" для повторной игры:')
            if input().lower() == 'да':
                cnt = 0
            else:
                break
    else:
        print('Неверный ввод. А может быть все-таки введем целое число от 1 до 100?')

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')