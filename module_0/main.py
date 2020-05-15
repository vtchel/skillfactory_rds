#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from argparse import ArgumentParser


MAX_INT = 100
RANDOM_SEED = 1


def game_core_v1(number):
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, MAX_INT)  # предполагаемое число
        if number == predict:
            return (count)  # выход из цикла, если угадали


def game_core_v2(number):
    """Простой перебор.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 0
    while count != number:
        count += 1
    return count         # выход из цикла, если угадали


def game_core_v3(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, MAX_INT)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count         # выход из цикла, если угадали


def game_core_v4(number):
    """Реализация метода деления пополам.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    start = 1
    end = MAX_INT
    predict = (start + end)//2          # определеяем середину, округление в меньшую сторону
    while number != predict:
        count += 1
        if number > predict:
            start = predict             # сокращаем интервал, переносим начало
            predict = (start + end)//2
        elif number < predict:
            end = predict               # сокращаем интервал, переносим конец
            predict = (start + end)//2
    return count                        # выход из цикла, если угадали


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(RANDOM_SEED)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, MAX_INT, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


# запускаем
if __name__ == '__main__':
    parser = ArgumentParser('python3 main.py',
                            description='''Игра Угадай число. Без аргументов запуск интерактивной части.''')
    parser.add_argument('--bench', dest='bench',
                        action='store_true', help='Запуск теста алгоритмов поиска')
    args = parser.parse_args()

    if args.bench:
        print('Тест game_core_v1: ', end='')
        score_game(game_core_v1)

        print('Тест game_core_v2: ', end='')
        score_game(game_core_v2)

        print('Тест game_core_v3: ', end='')
        score_game(game_core_v3)

        print('Тест game_core_v4: ', end='')
        score_game(game_core_v4)
    else:
        # Запрос числа пользователя в интервале от 1 до 99.
        number = int(input('Загадайте число от 1 до 99:\n'))

        # Запуск
        score_count = game_core_v4(number)
        print(f'Алгоритм угадал число за {score_count} попыток.')

