from typing import List

def split_words(text:str)->List[str]:
    """Разделяет слова в полученной строке
    Возвращает список слов"""
    text = text.replace('\\n', '_').replace('\\t', '_')
    razdeliteli = "«_.,;:!?»"
    for char in razdeliteli:
        text = text.replace(char, '_')
    words = [word for word in text.split('_') if word]
    return words

def find_alpha_digit_sign_words(words:List)->List[str]:
    """Ищет слова, имеющие знак, букву и цифру
    Возвращает список найденных слов"""
    special = []
    
    for word in words:
        bukva = False
        cifra = False
        znak = False
        for char in word:
            if char.isalpha():
                bukva = True
            elif char.isdigit():
                cifra = True
            else:
                znak = True
        
        if bukva == True and cifra == True and znak == True:
            special.append(word)
    return special

def print_alpha_digit_sign_words(special:List)->None:
    """Выводит слова имеющие знак, букву и цифру"""
    if not special:
        print("Слова со знаком, буквой и цифрой в данной строке отсутствуют :(")
    else:
        print("Слова со знаком, буквой и цифрой:", " ".join(special))

def find_symmetric_words(words:List)->List[str]:
    """Ищет симметричные слова
    Возвращает список найденных слов"""
    symmetric = []
    for word in words:
        if word == word[::-1]:
            symmetric.append(word)
    return symmetric

def find_max_digits_in_symmetric_words(symmetric:List)->List[str]:
    """Ищет симметричных слова с максимальным количеством цифр
    Возвращает список симметричных слов с максимальным количеством цифр"""
    if not symmetric:
        return []
    max_nums = 0
    result_words = []
    for word in symmetric:
        num_count = 0
        for char in word:
            if char >= '0' and char <= '9':
                num_count += 1
        if num_count > max_nums:
            max_nums = num_count
            result_words = [word]
        elif num_count == max_nums and num_count > 0:
            result_words.append(word)
    return result_words

def print_max_digits_in_symmetric_words(result_words:List)->None:
    """Выводит симметричные слова с максимальным количеством цифр"""
    if not result_words:
        print("Симметричные слова с максимальным количеством цифр в данной строке отсутствуют :(")
    else:
        result_str = " ".join(result_words)
        print("Симметричные слова с максимальным количеством цифр:", result_str)


def main():

    text = input("\nВведите строку для анализа: ")
    words = split_words(text)
    special_words = find_alpha_digit_sign_words(words)
    print_alpha_digit_sign_words(special_words)
    symmetric_words = find_symmetric_words(words)
    result = find_max_digits_in_symmetric_words(symmetric_words)
    print_max_digits_in_symmetric_words(result)

if __name__ == "__main__":
    main()


    help(split_words)
    assert split_words("word1;word2,word3") == ["word1", "word2", "word3"], "Тест 1.1: Ошибка в разделении слов"
    assert split_words("«hello»world") == ["hello", "world"], "Тест 1.2: Ошибка с кавычками"
    assert split_words("test1;test2:test3!test4?test5") == ["test1", "test2", "test3", "test4", "test5"], "Тест 1.3: Ошибка с разными разделителями"
    assert split_words("") == [], "Тест 1.4: Ошибка с пустой строкой"
    assert split_words("one«two»three_four.five,six;seven:eight?nine") == ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], "Тест 1.5: Ошибка со всеми разделителями"
    assert split_words("word1;;word2,,word3::word4") == ["word1", "word2", "word3", "word4"], "Тест 1.6: Ошибка с повторяющимися разделителями"
    assert split_words("no delimiters") == ["no delimiters"], "Тест 1.7: Ошибка со строкой без разделителей"
    assert split_words("hello\\tworld\\ntest") == ["hello", "world", "test"], "Тест 1.8: Ошибка с escape-последовательностями"


    help(find_alpha_digit_sign_words)
    assert find_alpha_digit_sign_words(["abc123!", "hello", "123", "test!123"]) == ["abc123!", "test!123"], "Тест 2.1: Ошибка поиска специальных слов"
    assert find_alpha_digit_sign_words(["hello", "world", "123"]) == [], "Тест 2.2: Ошибка: найдены лишние специальные слова"
    assert find_alpha_digit_sign_words(["a1!", "b2@", "c3#"]) == ["a1!", "b2@", "c3#"], "Тест 2.3: Ошибка с множеством специальных слов"
    assert find_alpha_digit_sign_words(["only_letters", "only123", "only!@#"]) == [], "Тест 2.4: Ошибка с неполными словами"
    assert find_alpha_digit_sign_words(["test123!", "word456@", "abc789#"]) == ["test123!", "word456@", "abc789#"], "Тест 2.5: Ошибка со словами разной длины"
    assert find_alpha_digit_sign_words(["1a!", "2b@", "3c#"]) == ["1a!", "2b@", "3c#"], "Тест 2.6: Ошибка с короткими словами"
    assert find_alpha_digit_sign_words(["abc!123", "123!abc", "!abc123"]) == ["abc!123", "123!abc", "!abc123"], "Тест 2.7: Ошибка с разным порядком символов"
    assert find_alpha_digit_sign_words([""]) == [], "Тест 2.8: Ошибка с пустыми словами"


    help(find_symmetric_words)
    assert find_symmetric_words(["radar", "hello", "12321"]) == ["radar", "12321"], "Тест 3.1: Ошибка поиска симметричных слов"
    assert find_symmetric_words(["level", "madam", "pop"]) == ["level", "madam", "pop"], "Тест 3.2: Ошибка с палиндромами"
    assert find_symmetric_words(["hello", "world"]) == [], "Тест 3.3: Ошибка: найдены несимметричные слова"
    assert find_symmetric_words([]) == [], "Тест 3.4: Ошибка с пустым списком"
    assert find_symmetric_words(["a", "bb", "ccc", "dddd"]) == ["a", "bb", "ccc", "dddd"], "Тест 3.5: Ошибка с односимвольными словами"
    assert find_symmetric_words(["1234321", "abcba", "12321"]) == ["1234321", "abcba", "12321"], "Тест 3.6: Ошибка с числовыми палиндромами"
    assert find_symmetric_words(["racecar", "deified", "rotator"]) == ["racecar", "deified", "rotator"], "Тест 3.7: Ошибка со сложными палиндромами"
    assert find_symmetric_words(["not", "palindrome", "test"]) == [], "Тест 3.8: Ошибка с непалиндромами"
    

    help(find_max_digits_in_symmetric_words)
    assert find_max_digits_in_symmetric_words(["aa", "11", "1a1", "12321", "abcba"]) == ["12321"], "Тест 4.1: Ошибка поиска слова с макс цифрами"
    assert find_max_digits_in_symmetric_words(["123", "456", "789"]) == ["123", "456", "789"], "Тест 4.2: Ошибка с одинаковым количеством цифр"
    assert find_max_digits_in_symmetric_words(["abc", "def", "ghi"]) == [], "Тест 4.3: Ошибка: найдены слова без цифр"
    assert find_max_digits_in_symmetric_words(["1a1", "2b2", "3c3"]) == ["1a1", "2b2", "3c3"], "Тест 4.4: Ошибка с одинаковым количеством цифр в смешанных словах"
    assert find_max_digits_in_symmetric_words(["12345", "12", "123", "1234"]) == ["12345"], "Тест 4.5: Ошибка с разным количеством цифр"
    assert find_max_digits_in_symmetric_words(["1", "22", "333"]) == ["333"], "Тест 4.6: Ошибка с возрастающим количеством цифр"
    assert find_max_digits_in_symmetric_words(["a1a", "b22b", "c333c"]) == ["c333c"], "Тест 4.7: Ошибка с цифрами внутри палиндромов"
    assert find_max_digits_in_symmetric_words(["123454321", "12321", "1234321"]) == ["123454321"], "Тест 4.8: Ошибка с большими числовыми палиндромами"
