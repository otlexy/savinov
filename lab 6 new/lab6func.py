import math
from typing import List, Tuple, Union, Optional

def calculate_z1(x: float, y: float) -> Tuple[int, Union[float, str]]:
    """Вычисляет z1 с обработкой математических ошибок"""
    
    try:
        z1 = pow(math.cos(x), 4) + pow(math.sin(y), 2) + 0.25 * pow(math.sin(2 * x), 2) - 1
        return (1, z1)
        
    except ZeroDivisionError as e:
        return (2, "Div By Zero")
    except OverflowError as e:
        return (3, "Overflow")

def calculate_z2(x: float, y: float) -> Tuple[int, Union[float, str]]:
    """Вычисляет z2 с обработкой математических ошибок"""
    
    try:
        z2 = math.sin(y + x) * math.sin(y - x)
        return (1, z2)
        
    except ZeroDivisionError as e:
        return (2, "Div By Zero")
    except OverflowError as e:
        return (3, "Overflow")

def calculate_z3(x: float) -> Tuple[int, Union[float, str]]:
    """Вычисляет z3 = 1/x с обработкой математических ошибок"""
    
    try:
        if x == 0:
            return (2, "Div By Zero")
        
        # Проверка на очень маленькие значения
        if abs(x) < 1e-14:
            return (3, "Overflow")
        
        # Обычное вычисление
        result = 1 / x
        return (1, result)
        
    except OverflowError:
        return (3, "Overflow")
    except ZeroDivisionError:
        return (2, "Div By Zero")

def read_data_from_file(filename: str) -> Optional[List[Tuple[float, float]]]:
    """Читает данные из файла и преобразует в список координат"""
    
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

def format_number(value: float) -> str:
    """Форматирует число для вывода в таблице"""
    if value == 0:
        return "   0.000000   "
    
    if abs(value) < 0.0001 or abs(value) >= 1000000:
        return f"{value:12.6e}"
    else:
        return f"{value:12.6f}"

def write_results_to_file(filename: str, results: List[Tuple[Tuple[float, float], Tuple[Tuple, Tuple, Tuple]]]) -> bool:
    """Записывает результаты вычислений в файл в табличном формате"""
    
    try:
        with open(filename, "w", encoding="utf-8") as fo:

            fo.write("┌────────────┬────────────┬──────────────┬──────────────┬──────────────┐\n")
            fo.write("│     X      │     Y      │      Z1      │      Z2      │      Z3      │\n")
            
            for (x, y), (result_z1, result_z2, result_z3) in results:
                fo.write("├────────────┼────────────┼──────────────┼──────────────┼──────────────┤\n")
                

                if x == 0:
                    display_x = "  0.000000  "
                elif abs(x) < 0.0001 or abs(x) >= 1000000:
                    display_x = f"{x:12.6e}"
                else:
                    display_x = f"{x:12.6f}"
                

                if y == 0:
                    display_y = "  0.000000  "
                elif abs(y) < 0.0001 or abs(y) >= 1000000:
                    display_y = f"{y:12.6e}"
                else:
                    display_y = f"{y:12.6f}"
                

                code_z1, value_z1 = result_z1
                if code_z1 == 2:
                    display_z1 = " Div By Zero  "
                elif code_z1 == 3:
                    display_z1 = "   Overflow   "
                else:
                    if value_z1 == 0:
                        display_z1 = "   0.000000   "
                    elif abs(value_z1) < 0.0001 or abs(value_z1) >= 1000000:
                        display_z1 = f"{value_z1:14.6e}"
                    else:
                        display_z1 = f"{value_z1:14.6f}"
                

                code_z2, value_z2 = result_z2
                if code_z2 == 2:
                    display_z2 = " Div By Zero  "
                elif code_z2 == 3:
                    display_z2 = "   Overflow   "
                else:
                    if value_z2 == 0:
                        display_z2 = "   0.000000   "
                    elif abs(value_z2) < 0.0001 or abs(value_z2) >= 1000000:
                        display_z2 = f"{value_z2:14.6e}"
                    else:
                        display_z2 = f"{value_z2:14.6f}"
                

                code_z3, value_z3 = result_z3
                if code_z3 == 2:
                    display_z3 = " Div By Zero  "
                elif code_z3 == 3:
                    display_z3 = "   Overflow   "
                else:
                    if value_z3 == 0:
                        display_z3 = "   0.000000   "
                    elif abs(value_z3) < 0.0001 or abs(value_z3) >= 1000000:
                        display_z3 = f"{value_z3:14.6e}"
                    else:
                        display_z3 = f"{value_z3:14.6f}"
                
                fo.write(f"│{display_x}│{display_y}│{display_z1}│{display_z2}│{display_z3}│\n")
            
            fo.write("└────────────┴────────────┴──────────────┴──────────────┴──────────────┘\n")
            
        return True
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")
        return False

def process_data(data: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], Tuple[Tuple, Tuple, Tuple]]]:
    """Обрабатывает данные и вычисляет результаты для всех пар (x,y)"""
    
    results = []
    for x, y in data:
        result_z1 = calculate_z1(x, y)
        result_z2 = calculate_z2(x, y)
        result_z3 = calculate_z3(x)
        results.append(((x, y), (result_z1, result_z2, result_z3)))
    return results

def test_func():
    """Тестирует все функции с помощью assert"""
    
    print("Тестирование calculate_z3...")
    assert calculate_z3(0) == (2, "Div By Zero"), "Ошибка в calculate_z3: деление на 0"
    assert calculate_z3(2)[0] == 1, "Ошибка в calculate_z3: успешное выполнение"
    assert calculate_z3(0.5)[0] == 1, "Ошибка в calculate_z3: успешное выполнение с дробью"
    assert calculate_z3(1e-40)[0] == 3, "Ошибка в calculate_z3: 1e-40 должно вызывать Overflow"
    assert calculate_z3(1e-14)[0] == 3, "Ошибка в calculate_z3: 1e-14 должно вызывать Overflow"
    assert calculate_z3(1e-13)[0] == 1, "Ошибка в calculate_z3: 1e-13 должно работать нормально"
    
    print("Тестирование calculate_z1...")
    result = calculate_z1(0, 0)
    assert result[0] == 1, "Ошибка в calculate_z1: успешное выполнение"
    assert isinstance(result[1], float), "Ошибка в calculate_z1: результат не float"
    
    print("Тестирование calculate_z2...")
    result = calculate_z2(0, 0)
    assert result[0] == 1, "Ошибка в calculate_z2: успешное выполнение"
    assert isinstance(result[1], float), "Ошибка в calculate_z2: результат не float"
    
    print("Тестирование read_data_from_file...")
    with open("test_input.txt", "w", encoding="utf-8") as f:
        f.write("1.0 2.0\n3.0 4.0\n5.0 6.0\n")
    data = read_data_from_file("test_input.txt")
    assert data == [(1.0, 2.0), (3.0, 4.0), (5.0, 6.0)], "Ошибка в read_data_from_file: чтение данных"
    
    print("Все тесты пройдены успешно!")
