def binary_search(arr, target):
    """
    Выполняет бинарный поиск в отсортированном массиве.

    Параметры:
    - arr (list): Отсортированный целочисленный массив.
    - target (int): Искомый элемент.

    Возвращает:
    - int: Индекс искомого элемента в массиве, если найден, в противном случае -1.

    """
    if not arr or not isinstance(arr, list):
        return -1  # Пустой массив или некорректный вход

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_value = arr[mid]

        if mid_value == target:
            return mid  # Найден искомый элемент, возвращаем индекс
        elif mid_value < target:
            low = mid + 1  # Искомый элемент находится справа от середины
        else:
            high = mid - 1  # Искомый элемент находится слева от середины

    return -1  # Элемент не найден в массиве


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Пример использования
    my_array = [7, 8, 9]
    target_element = 7

    result = binary_search(my_array, target_element)

    if result != -1:
        print(f"Элемент {target_element} найден в массиве. Индекс: {result}")
    else:
        print(f"Элемент {target_element} не найден в массиве.")
