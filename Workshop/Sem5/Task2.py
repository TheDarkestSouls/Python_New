# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все 
# конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому 
# игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint


candys = 2021
player1 = 0
player2 = 0
go_first = int(randint(1, 2))

while candys > 0:
    if go_first == 1:
        go_first = 2
        print(candys, ' left in the bowl.')
        player1 = int(input('How many candys P1 wish to take? '))
        if player1 > 28:
            player1 = 28
        candys -= player1
        if not candys:
            print('Player 1 wins!')
    else:
        go_first = 1
        print(candys, ' left in the bowl.')
        player2 = int(input('How many candys P2 wish to take? '))
        if player2 > 28:
            player2 = 28
        candys -= player2
        if not candys:
            print('Player 2 wins!')