from functions import *

def main():
    n = input_array_size()
    mas = create_array(n)
    min_index = find_minimal_element_index(mas)
    sum_between_elements, first_neg, second_neg = sum_elements_between_negatives(mas)
    transformed_mas = first_module_elements_less_1_second_others_array(mas)
    print_results(mas, min_index, sum_between_elements, first_neg, second_neg, transformed_mas)


if __name__ == "__main__":
    main()
