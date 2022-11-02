"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    high = 100 # верхнее значение рассматриваемого интервала
    low = 1 # нижнее значение интервала

    while True:
        count += 1
        predict_number = (low+high)//2  # предполагаемое число - середина интервала
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            low = predict_number+1 # если число БОЛЬШЕ на следующем шаге рассматриваем верхнюю половину интервала
        else: high = predict_number-1 # если число МЕНЬШЕ на следующем шаге рассматриваем нижнюю половину интервала
            
            
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
