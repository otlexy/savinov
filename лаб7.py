import random
import timeit
import numpy as np


# Функция 1: Создание матрицы как список списков
def make_matrix_list(rows, cols, min_val, max_val):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            num = random.randint(min_val, max_val)
            row.append(num)
        matrix.append(row)
    return matrix


# Функция 2: Создание матрицы через NumPy
def make_matrix_numpy(rows, cols, min_val, max_val):
    return np.random.randint(min_val, max_val + 1, size=(rows, cols))


# Функция 3: Характеристики столбцов для списков
def calculate_column_characteristics_list(matrix):
    if not matrix:
        return []
    
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    result = []
    
    for col in range(cols_count):
        sum_negative_odd = 0
        for row in range(rows_count):
            value = matrix[row][col]
            # Проверяем: отрицательное И нечетное
            if value < 0 and value % 2 != 0:
                sum_negative_odd += abs(value)
        result.append(sum_negative_odd)
    
    return result


# Функция 4: Характеристики столбцов для NumPy
def calculate_column_characteristics_numpy(matrix):
    if matrix.size == 0:
        return np.array([])
    
    # Находим отрицательные нечетные элементы
    mask = (matrix < 0) & (matrix % 2 != 0)
    
    # Берем модуль там, где mask=True, иначе 0
    masked_matrix = np.where(mask, np.abs(matrix), 0)
    
    # Суммируем по столбцам
    result = np.sum(masked_matrix, axis=0)
    
    return result


# Функция 5: Перестановка столбцов для списков
def rearrange_columns_by_characteristics_list(matrix, characteristics):
    if not matrix:
        return matrix, []
    
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    
    # Получаем порядок столбцов по возрастанию характеристик
    order = list(range(cols_count))
    order.sort(key=lambda x: characteristics[x])
    
    # Создаем новую матрицу
    new_matrix = []
    for i in range(rows_count):
        new_row = []
        for new_col_index in order:
            new_row.append(matrix[i][new_col_index])
        new_matrix.append(new_row)
    
    return new_matrix, order


# Функция 6: Перестановка столбцов для NumPy
def rearrange_columns_by_characteristics_numpy(matrix, characteristics):
    if matrix.size == 0:
        return matrix, np.array([])
    
    # Получаем порядок столбцов
    order = np.argsort(characteristics)
    
    # Переставляем столбцы
    new_matrix = matrix[:, order]
    
    return new_matrix, order


# Функция 7: Суммы столбцов с отрицательными элементами для списков
def sum_columns_with_negative_list(matrix):
    if not matrix:
        return []
    
    rows_count = len(matrix)
    cols_count = len(matrix[0])
    result = []
    
    for col in range(cols_count):
        has_negative = False
        col_sum = 0
        
        for row in range(rows_count):
            value = matrix[row][col]
            col_sum += value
            if value < 0:
                has_negative = True
        
        if has_negative:
            result.append(col_sum)
        else:
            result.append(None)
    
    return result


# Функция 8: Суммы столбцов с отрицательными элементами для NumPy
def sum_columns_with_negative_numpy(matrix):
    if matrix.size == 0:
        return np.array([])
    
    # Проверяем, есть ли в столбцах отрицательные
    has_negative = np.any(matrix < 0, axis=0)
    
    # Считаем суммы всех столбцов
    sums = np.sum(matrix, axis=0)
    
    # Там где нет отрицательных, ставим None
    result = []
    for i in range(len(sums)):
        if has_negative[i]:
            result.append(sums[i])
        else:
            result.append(None)
    
    return np.array(result)


# Функция 9: Печать матрицы
def print_small_matrix(matrix, limit=10):
    # Проверяем тип матрицы
    if isinstance(matrix, np.ndarray):
        rows, cols = matrix.shape
    else:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
    
    # Если матрица большая - не печатаем
    if rows > limit or cols > limit:
        print(f"Матрица {rows}x{cols} (слишком большая для печати)")
        return
    
    # Печатаем матрицу
    if isinstance(matrix, np.ndarray):
        for i in range(rows):
            for j in range(cols):
                print(f"{matrix[i][j]:6}", end=" ")
            print()
    else:
        for i in range(rows):
            for j in range(cols):
                print(f"{matrix[i][j]:6}", end=" ")
            print()


# Функция 10: Печать характеристик
def print_characteristics(characteristics):
    print("Характеристики столбцов:")
    for i, value in enumerate(characteristics):
        print(f"  Столбец {i}: {value}")


# Функция 11: Печать сумм столбцов
def print_column_sums(column_sums):
    print("\nСуммы в столбцах (только с отрицательными числами):")
    for i, value in enumerate(column_sums):
        if value is not None:
            print(f"  Столбец {i}: {value}")
        else:
            print(f"  Столбец {i}: нет отрицательных чисел")


# Основная программа
def main():
    # Параметры матрицы
    rows = 5
    cols = 6
    
    matrix_list = make_matrix_list(rows, cols, -20, 20)
    print_small_matrix(matrix_list)
    
    # 2. Считаем характеристики
    chars_list = calculate_column_characteristics_list(matrix_list)
    print_characteristics(chars_list)
    
    # 3. Переставляем столбцы
    new_matrix_list, order_list = rearrange_columns_by_characteristics_list(matrix_list, chars_list)
    print("\nМатрица после перестановки:")
    print_small_matrix(new_matrix_list)
    
    # 4. Суммы столбцов с отрицательными
    print("\n4. Суммы столбцов, где есть отрицательные числа:")
    sums_list = sum_columns_with_negative_list(matrix_list)
    print_column_sums(sums_list)
    
    # 1. Создаем матрицу
    matrix_numpy = make_matrix_numpy(rows, cols, -20, 20)
    print_small_matrix(matrix_numpy)
    
    # 2. Считаем характеристики
    chars_numpy = calculate_column_characteristics_numpy(matrix_numpy)
    print_characteristics(chars_numpy)
    
    # 3. Переставляем столбцы
    new_matrix_numpy, order_numpy = rearrange_columns_by_characteristics_numpy(matrix_numpy, chars_numpy)
    print("\nМатрица после перестановки:")
    print_small_matrix(new_matrix_numpy)
    
    # 4. Суммы столбцов с отрицательными
    print("\n4. Суммы столбцов, где есть отрицательные числа:")
    sums_numpy = sum_columns_with_negative_numpy(matrix_numpy)
    print_column_sums(sums_numpy)
    
    print("\n" + "-" * 60)
    print("СРАВНЕНИЕ СКОРОСТИ")
    print("-" * 60)
    
    # Тестируем на разных размерах
    test_matrices = [
        (100, 100, "Маленькая (100x100)"),
        (300, 300, "Средняя (300x300)"),
        (500, 500, "Большая (500x500)")
    ]
    
    print("\nСравнение времени выполнения (в секундах):")
    print("Размер матрицы | Списки | NumPy")
    print("-" * 45)
    
    for rows, cols, name in test_matrices:
        print(f"\n{name}:")
        
        # Тестируем списки
        print("  Списки:")
        
        # Время создания
        start = timeit.default_timer()
        test_list = make_matrix_list(rows, cols, -100, 100)
        time_create_list = timeit.default_timer() - start
        
        # Время характеристик
        start = timeit.default_timer()
        chars_test = calculate_column_characteristics_list(test_list)
        time_chars_list = timeit.default_timer() - start
        "Пройти по всем элементам матрицы по столбцам
        "Проверить для каждого элемента два условия:
        "Число отрицательное? (value < 0)
        "Число нечётное? (value % 2 != 0)
        "Если оба условия истинны — добавить модуль числа к сумме для этого столбца
        "Вернуть массив/список сумм для каждого столбца
        
        
        print(f"    Создание: {time_create_list:.4f} сек")
        print(f"    Характеристики: {time_chars_list:.4f} сек")
        
        # Тестируем NumPy
        print("  NumPy:")
        
        # Время создания
        start = timeit.default_timer()
        test_numpy = make_matrix_numpy(rows, cols, -100, 100)
        time_create_numpy = timeit.default_timer() - start
        
        # Время характеристик
        start = timeit.default_timer()
        chars_test_np = calculate_column_characteristics_numpy(test_numpy)
        time_chars_numpy = timeit.default_timer() - start
        "Пройти по всем элементам матрицы по столбцам
        "Проверить для каждого элемента два условия:
        "Число отрицательное? (value < 0)
        "Число нечётное? (value % 2 != 0)
        "Если оба условия истинны — добавить модуль числа к сумме для этого столбца
        "Вернуть массив/список сумм для каждого столбца

        
        print(f"    Создание: {time_create_numpy:.4f} сек")
        print(f"    Характеристики: {time_chars_numpy:.4f} сек")



# Запуск программы
if __name__ == "__main__":
    main()
