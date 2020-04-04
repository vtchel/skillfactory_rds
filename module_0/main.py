#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

MAX_INT = 101
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
    """Простой перебор"""
    count = 0
    while count != number:
        count += 1
    return count


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


def get_median(start, end):
    res = int((end + start)/2)   # ищется сеередина и округляется в меньшую сторону
    # print(res)
    return res


def game_core_v4(number):
    """Делим на 2, определяем больше меньше"""
    count = 1
    start = 1
    end = MAX_INT
    predict = get_median(start, end)    # определеяем середину
    while number != predict:
        count += 1
        if number > predict:
            start = predict             # сокращаем интервал, переносим начало
            predict = get_median(start, end)
        elif number < predict:
            end = predict               # сокращаем интервал, переносим конец
            predict = get_median(start, end)
    return count         # выход из цикла, если угадали


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
score_game(game_core_v4)
