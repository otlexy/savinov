from math import *
from random import *
from typing import List
from typing import Tuple

def input_array_size()->int:
    """Считывает размер массива
    Возвращает обработанный размер массива"""
    n = int(input("Элементов в массиве(N<=30) N: ")) 
    if n > 30: 
        n = 30 
    elif n < 5: 
        n = 5
    return n

def create_array(n:int)->List[float]:
    """Создает, выводит и возвращает начальный массив"""
    print("Начальное состояние") 
    mas = [] 
    for i in range(n): 
        mas.append(uniform(-5, 5)) 
        print("{0: 7.3f}".format(mas[i]), end=" ") 
    print()
    return mas

def find_minimal_element_index(mas:List[float])->int:
    """Ищет номер минимального элемента
    Возвращает номер минимального элемента"""
    min_index = 0
    for i in range(1, len(mas)):
        if mas[i] < mas[min_index]:
            min_index = i
    return min_index

def sum_elements_between_negatives(mas:List[float])->Tuple[float,int,int]:
    """Ищет суммы элементов между первым и вторым отрицательными элементами
    Возвращает сумму элементов между первым и вторым отрицательными элементами"""
    first_negative = -1
    second_negative = -1
    for i in range(len(mas)):
        if mas[i] < 0:
            first_negative = i
            break
    if first_negative != -1:
        for i in range(first_negative + 1, len(mas)):
            if mas[i] < 0:
                second_negative = i
                break
    
    sum_between_elements = 0.0
    if first_negative != -1 and second_negative != -1 and second_negative - first_negative > 1:
        for i in range(first_negative + 1, second_negative):
            sum_between_elements += mas[i]
    
    return sum_between_elements, first_negative, second_negative

def first_module_elements_less_1_second_others_array(mas:List[float])->List[float]:
    """Преобразовывает массив: сначала элементы с |x|<=1, потом остальные
    Возвращает преобразованный массив"""
    group1 = []
    group2 = []
    
    for element in mas:
        if abs(element) <= 1:
            group1.append(element)
        else:
            group2.append(element)
    
    return group1 + group2

def print_results(mas, min_index, sum_between, first_neg, second_neg, transformed_mas):
    """Выводит результаты"""
    print("\nРезультаты:")
    print(f"1. Индекс минимального элемента: {min_index}")
    print(f"   Минимальный элемент: {mas[min_index]:7.3f}")
    
    print(f"2. Сумма между отрицательными элементами: {sum_between:7.3f}")
    if first_neg != -1 and second_neg != -1:
        print(f"   Первый отрицательный: индекс {first_neg}, значение {mas[first_neg]:7.3f}")
        print(f"   Второй отрицательный: индекс {second_neg}, значение {mas[second_neg]:7.3f}")
    else:
        print("   Недостаточно отрицательных элементов")
    
    print("Преобразованный массив:")
    for i in range(len(transformed_mas)):
        print("{0: 7.3f}".format(transformed_mas[i]), end=" ") 
    print()
