from functions import *

help(find_minimal_element_index)
# 1. Проверка нахождения минимального элемента в конце массива
assert find_minimal_element_index([5.0, 3.0, -2.0, 1.0, -5.0]) == 4
# 2. Проверка нахождения минимального положительного элемента в середине массива
assert find_minimal_element_index([1.5, 2.0, 0.5, 3.0]) == 2
# 3. Проверка работы с массивом из отрицательных чисел
assert find_minimal_element_index([-1.0, -2.0, -3.0, -4.0]) == 3
# 4. Проверка обработки массива из одного элемента
assert find_minimal_element_index([10.0]) == 0
# 5. Проверка случая с несколькими одинаковыми минимальными значениями
assert find_minimal_element_index([2.0, 1.0, 2.0, 1.0]) == 1
# 6. Проверка работы с нулевыми и отрицательными значениями
assert find_minimal_element_index([0.0, -0.5, 0.5, -1.0]) == 3
# 7. Проверка нахождения минимального элемента среди положительных чисел
assert find_minimal_element_index([3.5, 2.1, 4.8, 1.9]) == 3
# 8. Проверка нахождения минимального отрицательного числа среди отрицательных
assert find_minimal_element_index([-1.5, -1.0, -2.0, -0.5]) == 2


help(sum_elements_between_negatives)
# 9. Проверка обычного случая с двумя отрицательными элементами и элементами между ними
sum1, first1, second1 = sum_elements_between_negatives([2.0, -1.0, 3.0, 4.0, -2.0])
assert abs(sum1 - 7.0) < 0.001 and first1 == 1 and second1 == 4
# 10. Проверка случая отсутствия отрицательных элементов
sum2, first2, second2 = sum_elements_between_negatives([1.0, 2.0, 3.0, 4.0])
assert abs(sum2 - 0.0) < 0.001 and first2 == -1 and second2 == -1
# 11. Проверка случая, когда отрицательные элементы идут подряд
sum3, first3, second3 = sum_elements_between_negatives([-1.0, 2.0, -3.0])
assert abs(sum3 - 2.0) < 0.001 and first3 == 0 and second3 == 2
# 12. Проверка случая с одним отрицательным элементом
sum4, first4, second4 = sum_elements_between_negatives([-1.0, 1.0, 2.0, 3.0])
assert abs(sum4 - 0.0) < 0.001 and first4 == 0 and second4 == -1
# 13. Проверка случая с тремя отрицательными элементами
sum5, first5, second5 = sum_elements_between_negatives([-1.5, 2.0, 3.0, -2.5, 4.0, -3.0])
assert abs(sum5 - 5.0) < 0.001 and first5 == 0 and second5 == 3
# 14. Проверка случая с чередующимися отрицательными элементами
sum6, first6, second6 = sum_elements_between_negatives([1.0, -2.0, 3.0, -4.0, 5.0, -6.0])
assert abs(sum6 - 3.0) < 0.001 and first6 == 1 and second6 == 3
# 15. Проверка случая, когда отрицательные элементы идут в начале массива
sum7, first7, second7 = sum_elements_between_negatives([-1.0, -2.0, 3.0, 4.0])
assert abs(sum7 - 0.0) < 0.001 and first7 == 0 and second7 == 1
# 16. Проверка случая с дробными числами и вычислением суммы
sum8, first8, second8 = sum_elements_between_negatives([0.5, -1.0, 1.5, 2.5, -2.0, 3.0])
assert abs(sum8 - 4.0) < 0.001 and first8 == 1 and second8 == 4


help(first_module_elements_less_1_second_others_array)
#17. Проверка разделения массива на две группы: |x|<=1 и |x|>1
transformed1 = first_module_elements_less_1_second_others_array([2.5, 0.5, -1.5, 0.2])
assert len(transformed1) == 4
assert all(abs(x) <= 1 for x in transformed1[:2])
assert all(abs(x) > 1 for x in transformed1[2:])

#18. Проверка случая, когда все элементы имеют |x|<=1
transformed2 = first_module_elements_less_1_second_others_array([0.1, -0.5, 0.8])
assert len(transformed2) == 3
assert all(abs(x) <= 1 for x in transformed2)

#19. Проверка случая, когда все элементы имеют |x|>1
transformed3 = first_module_elements_less_1_second_others_array([2.0, -3.0, 4.0])
assert len(transformed3) == 3
assert all(abs(x) > 1 for x in transformed3)
    
#20. Проверка случая с граничными значениями (1 и -1)
transformed4 = first_module_elements_less_1_second_others_array([1.0, -1.0, 0.5, -0.5])
assert len(transformed4) == 4
assert all(abs(x) <= 1 for x in transformed4)

#21. Проверка случая с нулевым значением и границей модуля
transformed5 = first_module_elements_less_1_second_others_array([0.0, 1.0, -1.0, 2.0])
assert len(transformed5) == 4
assert all(abs(x) <= 1 for x in transformed5[:3])
assert all(abs(x) > 1 for x in transformed5[3:])

#22. Проверка сложного случая со смешанными значениями
transformed6 = first_module_elements_less_1_second_others_array([1.5, -2.5, 0.3, -1.8, 0.9])
assert len(transformed6) == 5
assert all(abs(x) <= 1 for x in transformed6[:2])
assert all(abs(x) > 1 for x in transformed6[2:])

#23. Проверка случая с дробными числами в пределах модуля
transformed7 = first_module_elements_less_1_second_others_array([0.2, 0.4, 0.6, 0.8])
assert len(transformed7) == 4
assert all(abs(x) <= 1 for x in transformed7)

#24. Проверка случая с большими по модулю отрицательными числами
transformed8 = first_module_elements_less_1_second_others_array([3.0, -4.0, 5.0, -6.0])
assert len(transformed8) == 4
assert all(abs(x) > 1 for x in transformed8)

