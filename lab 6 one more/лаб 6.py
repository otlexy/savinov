from math import sin, cos
from decimal import (
    Decimal,
    InvalidOperation,
    DivisionByZero,
    Overflow,
    getcontext
)
from typing import Union
import sys

# Устанавливаем высокую точность для поддержки очень больших/малых чисел
getcontext().prec = 1000

# Определяем границы для переполнения
MAX_SAFE_VALUE = Decimal('1e+1000')  # Максимальное безопасное значение
MIN_SAFE_VALUE = Decimal('1e-1000')  # Минимальное безопасное значение

def safe_inverse_decimal(x: Union[int, float, str, Decimal], original_str: str = None) -> str:
    """
    Вычисляет 1/x с использованием Decimal и возвращает результат в виде строки
    без научной нотации, если это возможно.

    Обрабатывает:
    - деление на ноль,
    - переполнение (слишком большое значение),
    - некорректный ввод.

    Args:
        x: число в виде int, float, str или Decimal.
        original_str: оригинальная строковая запись числа

    Returns:
        str: результат в обычной десятичной записи или сообщение об ошибке.
    """
    # 1. Преобразование входного значения в Decimal
    try:
        # Особый случай: если float(x) == 0.0, но есть оригинальная строка с научной нотацией
        if original_str and 'e-' in original_str.lower():
            try:
                # Пытаемся создать Decimal из оригинальной строки (для очень маленьких чисел)
                x_decimal = Decimal(original_str)
                # Проверяем, не слишком ли маленькое число
                if abs(x_decimal) < MIN_SAFE_VALUE and not x_decimal.is_zero():
                    return "Ошибка переполнения"
            except:
                # Если не получилось, используем стандартный путь
                if isinstance(x, float):
                    x_decimal = Decimal(str(x))
                else:
                    x_decimal = Decimal(x)
        else:
            if isinstance(x, float):
                x_decimal = Decimal(str(x))
            else:
                x_decimal = Decimal(x)
    except (InvalidOperation, TypeError, ValueError):
        return "Ошибка: входное значение не является числом"

    # 2. Проверка на ноль
    if x_decimal.is_zero():
        return "Ошибка деления на ноль"

    # 3. Проверка на слишком маленькое значение (вызовет слишком большое 1/x)
    if abs(x_decimal) < MIN_SAFE_VALUE:
        return "Ошибка переполнения"

    # 4. Вычисление 1/x с обработкой исключений
    try:
        result = Decimal(1) / x_decimal
    except DivisionByZero:
        return "Ошибка деления на ноль"
    except Overflow:
        return "Ошибка переполнения"
    except InvalidOperation:
        return "Ошибка: недопустимая операция"

    # 5. Дополнительная проверка на бесконечность (если traps[Overflow]=False)
    if result.is_infinite():
        return "Ошибка переполнения3"

    # 6. Проверка на слишком большое значение результата
    if abs(result) > MAX_SAFE_VALUE:
        return "Ошибка переполнения"

    # 7. Форматирование без 'e'
    try:
        s = format(result, 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        
        # ПРОВЕРКА: считаем сколько знаков после точки
        if '.' in s:
            # Разделяем число на части: до точки и после точки
            parts = s.split('.')
            # parts[1] - это часть после точки
            digits_after_point = len(parts[1])
            
            # Если после точки больше 1000 цифр - это переполнение
            if digits_after_point > 1000:
                return "Ошибка переполнения"

        return s
    except Exception:
        # Fallback на случай неожиданных ошибок форматирования
        return str(result)

def safe_calculate_z1_z2(a: float, b: float) -> tuple:
    """
    Безопасное вычисление z1 и z2 с обработкой переполнения и деления на ноль.
    
    Returns:
        tuple: (z1, z2) или (None, None) в случае ошибки
    """
    try:
        # Первая формула: z1 = (sin(a) + cos(2*b - a))/(cos(a) - sin(2*b - a))
        denominator1 = cos(a) - sin(2*b - a)
        
        # Проверка знаменателя на близость к нулю (риск переполнения)
        if abs(denominator1) < 1e-15:
            z1 = None  # Будет обработано как ошибка
        else:
            z1 = (sin(a) + cos(2*b - a)) / denominator1
            
            # Проверка на переполнение float
            if abs(z1) > 1e+308:
                z1 = None

        # Вторая формула: z2 = (1 + sin(2*b))/(cos(2*b))
        denominator2 = cos(2*b)
        
        # Проверка знаменателя на близость к нулю (риск переполнения)
        if abs(denominator2) < 1e-15:
            z2 = None  # Будет обработано как ошибка
        else:
            z2 = (1 + sin(2*b)) / denominator2
            
            # Проверка на переполнение float
            if abs(z2) > 1e+308:
                z2 = None

        return z1, z2
        
    except ZeroDivisionError:
        return None, None
    except OverflowError:
        return None, None
    except Exception:
        return None, None

# Рабочая функция для расчета
def calculate_values(a, b, original_a_str=None):
    try:
        # Безопасное вычисление z1 и z2
        z1, z2 = safe_calculate_z1_z2(a, b)
        
        # Если z1 или z2 равны None, значит была ошибка
        if z1 is None:
            z1_str = "Overflow"
        else:
            z1_str = z1
            
        if z2 is None:
            z2_str = "Overflow"
        else:
            z2_str = z2

        # Третья формула: z3 = 1/a с использованием Decimal для точности
        z3 = safe_inverse_decimal(a, original_a_str)

        return z1_str, z2_str, z3

    except ZeroDivisionError:
        # Обработка деления на ноль в формулах z1 или z2
        return "Div by zero", "Div by zero", "Div by zero"
    except Exception as e:
        # Обработка других ошибок
        return f"Error", f"Error", f"Error: {str(e)[:20]}"

# Открываем файлы для чтения и записи с использованием with
try:
    with open("lab1_pb_in.txt", "rt", encoding="utf-8") as fi, open("lab1_pb_ou.txt", "wt", encoding="utf-8") as fo:

        # Считываем все строки из файла
        lines = fi.readlines()

        # Фильтруем строки, которые можно преобразовать в пару чисел
        test_cases = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):  # Игнорируем комментарии
                try:
                    # Разделяем строку на части и проверяем, что есть хотя бы 2 элемента
                    parts = line.split()
                    if len(parts) >= 2:  # Проверяем, что есть как минимум 2 числа
                        a_str, b_str = parts[0], parts[1]
                        a = float(a_str)
                        b = float(b_str)
                        test_cases.append((a, b, a_str))  # Сохраняем оригинальную строку
                except ValueError:
                    # Игнорируем строки, которые нельзя преобразовать в числа
                    continue

        # Печатаем заголовок таблицы в файл
        fo.write("┌─────┬─────────────┬─────────┬─────────────┬─────────────┬───────────────────────┐\n")
        fo.write("│  №  │      α      │    β    │     z1      │     z2      │            z3         │\n")
        fo.write("├─────┼─────────────┼─────────┼─────────────┼─────────────┼───────────────────────┤\n")

        # Обрабатываем каждую строку входных данных
        for i, (a, b, original_a_str) in enumerate(test_cases, start=1):
            z1, z2, z3 = calculate_values(a, b, original_a_str)

            # Улучшенное форматирование для α
            if original_a_str and 'e-' in original_a_str.lower() and a == 0:
                # Если число было в научной нотации и стало 0, показываем оригинальное значение
                try:
                    # Пытаемся отформатировать оригинальную строку
                    a_str = f"{original_a_str:>11}"
                except:
                    a_str = f"{a:>11.2f}"
            elif original_a_str and 'e-' in original_a_str.lower():
                # Для чисел в научной нотации используем научный формат вывода
                try:
                    a_value = float(original_a_str)
                    a_str = f"{a_value:>11.2e}"
                except:
                    a_str = f"{a:>11.2f}"
            elif a != 0 and abs(a) < 0.001:
                a_str = f"{a:>11.2e}"
            else:
                a_str = f"{a:>11.2f}"

            # Форматирование для β
            if b != 0 and abs(b) < 0.001:
                b_str = f"{b:>7.2e}"
            else:
                b_str = f"{b:>7.2f}"

            # Подготовка строковых значений с фиксированной шириной
            if isinstance(z1, (int, float)):
                z1_str = f"{z1:>11.4f}"
            else:
                z1_str = f"{str(z1):>11}" if z1 else "Overflow".rjust(11)

            if isinstance(z2, (int, float)):
                z2_str = f"{z2:>11.4f}"
            else:
                z2_str = f"{str(z2):>11}" if z2 else "Overflow".rjust(11)

            # Специальное форматирование для z3 (используем safe_inverse_decimal)
            if isinstance(z3, (int, float)):
                # Если z3 - число, форматируем его
                z3_str = f"{z3:>21.4f}"
            else:
                # Если z3 - строка (результат safe_inverse_decimal или сообщение об ошибке)
                if z3 == "Ошибка деления на ноль" or z3 == "Div by zero":
                    z3_str = "Div by zero".rjust(21)
                elif z3 == "Ошибка переполнения" or z3 == "Overflow":
                    z3_str = "Overflow".rjust(21)
                elif "Error" in z3:
                    # Сокращаем сообщения об ошибках
                    error_msg = z3.replace("Error: ", "")
                    if len(error_msg) > 15:
                        error_msg = error_msg[:12] + "..."
                    z3_str = error_msg.rjust(21)
                else:
                    # Пытаемся обрезать слишком длинный результат
                    if isinstance(z3, str) and len(z3) > 21:
                        # Если результат слишком длинный, показываем первые 18 символов и "..."
                        z3_str = f"{z3[:18]}...".rjust(21)
                    else:
                        z3_str = f"{str(z3):>21}"

            # Запись результатов в строку таблицы
            fo.write(f"│ {i:>3} │ {a_str} │ {b_str} │ {z1_str} │ {z2_str} │ {z3_str} │\n")

        # Печатаем нижнюю границу таблицы
        fo.write("└─────┴─────────────┴─────────┴─────────────┴─────────────┴───────────────────────┘\n")

except FileNotFoundError as e:
    print(f"Error: {str(e)}")
except Exception as e:
    print(f"Unexpected error: {str(e)}")
    
print("Результаты в файле lab1_pb_ou.txt")

