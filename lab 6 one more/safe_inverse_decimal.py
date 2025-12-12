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

def safe_inverse_decimal(x: Union[int, float, str, Decimal]) -> str:
    """
    Вычисляет 1/x с использованием Decimal и возвращает результат в виде строки
    без научной нотации, если это возможно.

    Обрабатывает:
    - деление на ноль,
    - переполнение (слишком большое значение),
    - некорректный ввод.

    Args:
        x: число в виде int, float, str или Decimal.

    Returns:
        str: результат в обычной десятичной записи или сообщение об ошибке.
    """
    # 1. Преобразование входного значения в Decimal
    try:
        if isinstance(x, float):
            # Преобразуем float через строку, чтобы избежать потерь точности
            x = Decimal(str(x))
        else:
            x = Decimal(x)
    except (InvalidOperation, TypeError, ValueError):
        return "Ошибка: входное значение не является числом"

    # 2. Проверка на ноль
    if x.is_zero():
        return "Ошибка деления на ноль"

    # 3. Вычисление 1/x с обработкой исключений
    try:
        result = Decimal(1) / x
    except DivisionByZero:
        return "Ошибка деления на ноль"
    except Overflow:
        return "Ошибка переполнения"
    except InvalidOperation:
        return "Ошибка: недопустимая операция"

    # 4. Дополнительная проверка на бесконечность (если traps[Overflow]=False)
    if result.is_infinite():
        return "Ошибка переполнения"

    # 5. Форматирование без 'e'
    try:
        s = format(result, 'f')
        if '.' in s:
            s = s.rstrip('0').rstrip('.')
        return s
    except Exception:
        # Fallback на случай неожиданных ошибок форматирования
        return str(result)


# ——————————————————————————————

if __name__ == "__main__":
    # Обычные случаи
    assert safe_inverse_decimal(2) == "0.5"
    assert safe_inverse_decimal(4) == "0.25"
    assert safe_inverse_decimal("3") == "0.3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333"
    

    # Целые результаты
    assert safe_inverse_decimal("0.5") == "2"
    assert safe_inverse_decimal("0.25") == "4"

    # Деление на ноль
    assert safe_inverse_decimal(0) == "Ошибка деления на ноль"
    assert safe_inverse_decimal(0.0) == "Ошибка деления на ноль"
    assert safe_inverse_decimal("0") == "Ошибка деления на ноль"
    assert safe_inverse_decimal("0.0") == "Ошибка деления на ноль"

    # Переполнение
    # для decimal.Decimal поведение управляется контекстом (decimal.getcontext()),
    # для float всё задано IEEE 754 (float это аппаратный тип с плавающей точкой двойной точности (IEEE 754)).
    # для float наименьшее положительное нормальное число ≈ 2.2250738585072014e-308
    # для float наибольшее положительное нормальное число ≈ 1.7976931348623157e+308
    #(см: sys.float_info.min и sys.float_info.max)
    # print(sys.float_info.min)
    # print(sys.float_info.max)
    
    assert safe_inverse_decimal("1e-1000000") == "Ошибка переполнения" # В Decimal (по умолчанию): переполнение только при 1 / 1e-1000000
    assert safe_inverse_decimal(1e-330) == "Ошибка деления на ноль"  # потому что передали float, а float(1e-330) == 0.0

    # Очень маленькое, но допустимое число
    res = safe_inverse_decimal("1e-500")
    assert res == "1" + "0" * 500  # 1 и 500 нулей

    # Очень большое, но допустимое число, передали строку, которую преобразовываем в формат decimal...
    # "1e-320" → Decimal понимает это как 1 × 10⁻³²⁰
    res = safe_inverse_decimal("1e+500")
    assert res == "0." + "0" * 499 + "1"

    # Некорректный ввод
    assert safe_inverse_decimal("abc") == "Ошибка: входное значение не является числом"
    assert safe_inverse_decimal([]) == "Ошибка: входное значение не является числом"

    # Отрицательные числа
    assert safe_inverse_decimal("-2") == "-0.5"
    assert safe_inverse_decimal("-0.1") == "-10"

    print("Все тесты пройдены!")

print(safe_inverse_decimal(0.5))
print(safe_inverse_decimal(3))
print(safe_inverse_decimal(0))
print(safe_inverse_decimal(0.0))
print(safe_inverse_decimal(1e-100))
print(safe_inverse_decimal(1e-200))
print(safe_inverse_decimal(1e-350))
print(safe_inverse_decimal(12))
print(safe_inverse_decimal("1e-1000000"))
print(safe_inverse_decimal("qwerty"))
