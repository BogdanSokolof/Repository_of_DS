import numpy as np

# Читал книгу по алгоритмам и мне недавно попался бинарный поиск,который идеально сюда подойдёт

def binary_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    
    count = 0
    low = 1
    high = 100
    
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if mid == number:
            break
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1
    
    return count

def score_game(predict_func) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        predict_func ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(predict_func(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN


    score_game(binary_predict)