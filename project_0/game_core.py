def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
  
    count = 1  
    low = 1  
    high = 100
    #делим диапазон возможных чисел пополам на каждой 
    #итерации и сравниваем среднее значение с загаданным число
    while low <= high:
        mid = (low + high) // 2 #вычисляем среднее значение
        if mid == number:  #если угадали, прерываем цикл
            break
        elif mid < number: #если ср знач меньше загаданного числа
            low = mid + 1 #нижняя граница сдвигается
        else:
            high = mid - 1 #вернхяя граница сдвигается ниже 
        count += 1 #считаем количество попыток

    return count

#Run 
if __name__ == '__main__':
    game_core_v3(int)