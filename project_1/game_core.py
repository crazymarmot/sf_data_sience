def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1   
    low = 1     #берем пороги макс и мин числ знач
    high = 100

    while low <= high:
        mid = (low + high) // 2 #высчитываем сред значение
        if mid == number: #если среднее и есть число, то прекращаем
            break
        elif mid < number: #если ср. значение меньше заданного числа
            low = mid + 1  #нижняя граница сдвигается на плюс один
        else:
            high = mid - 1 #верхняя граница сдвигается на минус один
        count += 1 #прибавляем кол-во попыток

    return count