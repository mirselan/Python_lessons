'''
Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота ""интеллектом""'''
############################################################################################
from random import choice

sweets = 2021
turn_temp = ['FirstGamer', 'SecondGamer']
turn = choice(turn_temp)

while sweets > 0:
    turn_1 = [i for i in turn_temp if i != turn][0]
    get = int(input(f'{turn_1}, how much sweets will you take? '))
    if get > 28:
        print(f'{turn_1}, you can take no more then 28 sweets at one time...')
        continue
    sweets -= get
    if sweets <= 0:
        print(f'{turn_1} is winner!')
        break
    else:
        turn_2 = [i for i in turn_temp if i != turn_1][0]
        get = int(input(f'{turn_2}, how much sweets will you take? '))
        if get > 28:
            print(f'{turn_2}, you can take no more then 28 sweets at one time...')
            get = int(input(f'{turn_2}, how much sweets will you take? '))
        sweets -= get
        if sweets <= 0:
            print(f'{turn_2} is winner!')
