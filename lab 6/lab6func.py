import math
from typing import List, Tuple, Union, Optional

def calculate_z1(x: float, y: float) -> Tuple[int, Union[float, str], str, str]:
    """Вычисляет z1 с обработкой математических ошибок
    
    Аргументы:
        x: Первое входное значение
        y: Второе входное значение
        
    Возвращает:
            Код ошибки (1-успех, 2-деление на 0, 3-переполнение)
            Значение выражения или текст ошибки
            Результат теста деления на 0
            Результат теста переполнения"""
    
    try:
        z1 = pow(math.cos(x), 4) + pow(math.sin(y), 2) + 0.25 * pow(math.sin(2 * x), 2) - 1
        
        division_test = test_division(0)
        overflow_test = test_division("overflow")
        
        return (1, z1, division_test[1], overflow_test[1])
        
    except ZeroDivisionError as e:
        return (2, "ZeroDivision", "N/A", "N/A")
    except OverflowError as e:
        return (3, "Overflow", "N/A", "N/A")

def calculate_z2(x: float, y: float) -> Tuple[int, Union[float, str], str, str]:
    """Вычисляет z2 с обработкой математических ошибок
    
    Аргументы:
        x: Первое входное значение
        y: Второе входное значение
        
    Возвращает:
            Код ошибки (1-успех, 2-деление на 0, 3-переполнение)
            Значение выражения или текст ошибки
            Результат теста деления на 0
            Результат теста переполнения"""
    
    try:
        z2 = math.sin(y + x) * math.sin(y - x)
        
        division_test = test_division(0)
        overflow_test = test_division("overflow")
        
        return (1, z2, division_test[1], overflow_test[1])
        
    except ZeroDivisionError as e:
        return (2, "ZeroDivision", "N/A", "N/A")
    except OverflowError as e:
        return (3, "Overflow", "N/A", "N/A")

def test_division(x: Union[float, str]) -> Tuple[int, str]:
    """Тестирует операцию деления на возможность ошибок
    
    Аргументы:
        x: Значение для тестирования или строка "overflow" для теста переполнения
        
    Возвращает:
            Код результата (1-успех, 2-деление на 0, 3-переполнение)
            Результат вычисления или текст ошибки"""
    
    try:
        if x == "overflow":
            result = math.exp(1000)
        else:
            result = 1 / x
        return (1, f"{result:.2e}")
    except ZeroDivisionError:
        return (2, "∞ (деление на 0)")
    except OverflowError:
        return (3, "OVERFLOW")

def read_data_from_file(filename: str) -> Optional[List[Tuple[float, float]]]:
    """Читает данные из файла и преобразует в список координат
    
    Аргументы:
        filename: Имя файла для чтения
        
    Возвращает:
            Список кортежей (x, y) или None при ошибке чтения"""
    
    data = []
    try:
        with open(filename, "r", encoding="utf-8") as fi:
            for line in fi:
                if line.strip() == "":
                    continue
                try:
                    parts = line.split()
                    if len(parts) >= 2:
                        x = float(parts[0])
                        y = float(parts[1])
                        data.append((x, y))
                except ValueError as e:
                    print(f"Ошибка преобразования данных в строке: {line.strip()} - {e}")
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None
    
    return data

def write_results_to_file(filename: str, results: List[Tuple[Tuple[float, float], Tuple[Tuple, Tuple]]]) -> bool:
    """Записывает результаты вычислений в файл в табличном формате
    
    Аргументы:
        filename: Имя файла для записи
        results: Список результатов в формате [((x,y), (result_z1, result_z2))]
        
    Возвращает:
        bool: True если запись успешна, False при ошибке"""
    
    try:
        with open(filename, "w", encoding="utf-8") as fo:
            fo.write("┌────────┬────────┬────────────┬────────────┬────────────────────┬──────────────────┐\n")
            fo.write("│   X    │   Y    │     Z1     │     Z2     │    Деление на 0    │   Переполнение   │\n")
            
            for (x, y), (result_z1, result_z2) in results:
                fo.write("├────────┼────────┼────────────┼────────────┼────────────────────┼──────────────────┤\n")
                code_z1, value_z1, div_z1, overflow_z1 = result_z1
                if code_z1 == 2:
                    display_z1 = "ДЕЛЕНИЕ НА 0"
                elif code_z1 == 3:
                    display_z1 = "ПЕРЕПОЛНЕНИЕ"
                else:
                    display_z1 = f"{value_z1:10.6f}"
                
                code_z2, value_z2, div_z2, overflow_z2 = result_z2
                if code_z2 == 2:
                    display_z2 = "ДЕЛЕНИЕ НА 0"
                elif code_z2 == 3:
                    display_z2 = "ПЕРЕПОЛНЕНИЕ"
                else:
                    display_z2 = f"{value_z2:10.6f}"
                
                fo.write(f"│ {x:6.2f} │ {y:6.2f} │ {display_z1:10} │ {display_z2:10} │ {div_z1:18} │ {overflow_z1:16} │\n")
            fo.write("└────────┴────────┴────────────┴────────────┴────────────────────┴──────────────────┘\n")    

            
        return True
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")
        return False

def process_data(data: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], Tuple[Tuple, Tuple]]]:
    """Обрабатывает данные и вычисляет результаты для всех пар (x,y)
    
    Аргументы:
        data: Список кортежей с входными данными [(x1,y1), (x2,y2), ...]
        
    Возвращает:
        List[Tuple[Tuple[float, float], Tuple[Tuple, Tuple]]]: 
            Список результатов в формате [((x,y), (result_z1, result_z2))]"""
    
    results = []
    for x, y in data:
        result_z1 = calculate_z1(x, y)
        result_z2 = calculate_z2(x, y)
        results.append(((x, y), (result_z1, result_z2)))
    return results

def test_func():
    """Тестирует все функции с помощью assert"""
    

    help (test_division)
    assert test_division(0) == (2, "∞ (деление на 0)"), "Ошибка в test_division: деление на 0"
    assert test_division("overflow") == (3, "OVERFLOW"), "Ошибка в test_division: переполнение"
    assert test_division(1)[0] == 1, "Ошибка в test_division: успешное выполнение"
    assert test_division(2)[0] == 1, "Ошибка в test_division: успешное выполнение"
    assert test_division(0.5)[0] == 1, "Ошибка в test_division: успешное выполнение с дробью"
    

    help (calculate_z1)
    result = calculate_z1(0, 0)
    assert result[0] == 1, "Ошибка в calculate_z1: успешное выполнение"
    assert isinstance(result[1], float), "Ошибка в calculate_z1: результат не float"
    assert result[2] == "∞ (деление на 0)", "Ошибка в calculate_z1: тест деления"
    assert result[3] == "OVERFLOW", "Ошибка в calculate_z1: тест переполнения"
    result = calculate_z1(math.pi/2, math.pi/2)
    assert result[0] == 1, "Ошибка в calculate_z1: специальные значения"

    
    help (calculate_z2)
    result = calculate_z2(0, 0)
    assert result[0] == 1, "Ошибка в calculate_z2: успешное выполнение"
    assert isinstance(result[1], float), "Ошибка в calculate_z2: результат не float"
    assert result[2] == "∞ (деление на 0)", "Ошибка в calculate_z2: тест деления"
    assert result[3] == "OVERFLOW", "Ошибка в calculate_z2: тест переполнения"
    result = calculate_z2(math.pi/4, math.pi/4)
    assert result[0] == 1, "Ошибка в calculate_z2: специальные значения"
    

    help (read_data_from_file)
    with open("test_input.txt", "w", encoding="utf-8") as f:
        f.write("1.0 2.0\n3.0 4.0\n5.0 6.0\n")
    data = read_data_from_file("test_input.txt")
    assert data == [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)], "Ошибка в read_data_from_file: чтение данных"
    assert read_data_from_file("nonexistent_file.txt") is None, "Ошибка в read_data_from_file: обработка отсутствующего файла"
    

    help (process_data)
    test_data = [(0, 0), (1, 1)]
    results = process_data(test_data)
    assert len(results) == 2, "Ошибка в process_data: количество результатов"
    for (x, y), (res_z1, res_z2) in results:
        assert len(res_z1) == 4, "Ошибка в process_data: формат результата z1"
        assert len(res_z2) == 4, "Ошибка в process_data: формат результата z2"
    

    help (write_results_to_file)
    test_results = [((0, 0), ((1, 0.5, "test1", "test2"), (1, 0.3, "test3", "test4")))]
    assert write_results_to_file("test_output.txt", test_results) == True, "Ошибка в write_results_to_file: запись файла"
    
    
    print("Все тесты пройдены успешно!")
