def make_words(s:str)->list[str]:
    """Создание слов из введённой строки"""
    razdeliteli = "«_.,;:\n\t!?»"
    for razdel in razdeliteli:
        s = s.replace(razdel, '|')
    words = [word for word in s.split('|') if word]
    return words

def find_special_words(words):
    """Поиск слов со знаком, буквой и цифрой"""
    special = ""
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
            special = special + word + ' '
    return special

def print_special(special):
    """Вывод слов со знаком, буквой и цифрой"""
    if special == "":
        print ("Слова со знаком, буквой и цифрой в данной строке отсутствуют :(")
    else:
        print("Слова со знаком, буквой и цифрой: ", special.strip())


def find_symmetric(words):
    """Поиск симметричных слов"""
    symmetric = []
    for word in words:
        if word == word[::-1]:
            symmetric.append(word)
    return symmetric

def find_max_num_in_symmetric(symmetric):
    """Поиск слов с максимальным количеством цифр в симметричных словах"""
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

def print_max_num_in_symmetric(result_words):
    """Вывод слов с максимальным количеством цифр в симметричных словах"""
    if not result_words:
        print("Симметричные слова с максимальным количеством цифр в данной строке отсутствуют :(")
    else:
        result_str = " ".join(result_words)
        print("Симметричные слова с максимальным количеством цифр: ", result_str)

def main():
    s = input("Введите строку: ")
    words = make_words(s)
    special_words = find_special_words(words)
    print_special(special_words)
    symmetric_words = find_symmetric(words)
    result = find_max_num_in_symmetric(symmetric_words)
    print_max_num_in_symmetric(result)

if __name__ == "__main__":
    main()

    print("\n1. Тестирование make_words...")
    assert make_words("word1;word2,word3") == ["word1", "word2", "word3"], "Тест 1.1: Ошибка в разделении слов"
    assert make_words("«hello»world") == ["hello", "world"], "Тест 1.2: Ошибка с кавычками"
    assert make_words("test1;test2:test3!test4?test5") == ["test1", "test2", "test3", "test4", "test5"], "Тест 1.3: Ошибка с разными разделителями"
    assert make_words("") == [], "Тест 1.4: Ошибка с пустой строкой"
    assert make_words("one«two»three_four.five,six;seven:eight?nine") == ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], "Тест 1.5: Ошибка со всеми разделителями"
    assert make_words("word1;;word2,,word3::word4") == ["word1", "word2", "word3", "word4"], "Тест 1.6: Ошибка с повторяющимися разделителями"
    assert make_words("no delimiters") == ["no delimiters"], "Тест 1.7: Ошибка со строкой без разделителей"
    assert make_words("a«b»c_d.e,f;g:h?i\nj\tk") == ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"], "Тест 1.8: Ошибка с управляющими символами"
    
    print("\n2. Тестирование find_special_words...")
    assert find_special_words(["abc123!", "hello", "123", "test!123"]).strip() == "abc123! test!123", "Тест 2.1: Ошибка поиска специальных слов"
    assert find_special_words(["hello", "world", "123"]) == "", "Тест 2.2: Ошибка: найдены лишние специальные слова"
    assert find_special_words(["a1!", "b2@", "c3#"]).strip() == "a1! b2@ c3#", "Тест 2.3: Ошибка с множеством специальных слов"
    assert find_special_words(["only_letters", "only123", "only!@#"]) == "", "Тест 2.4: Ошибка с неполными словами"
    assert find_special_words(["test123!", "word456@", "abc789#"]).strip() == "test123! word456@ abc789#", "Тест 2.5: Ошибка со словами разной длины"
    assert find_special_words(["1a!", "2b@", "3c#"]).strip() == "1a! 2b@ 3c#", "Тест 2.6: Ошибка с короткими словами"
    assert find_special_words(["abc!123", "123!abc", "!abc123"]).strip() == "abc!123 123!abc !abc123", "Тест 2.7: Ошибка с разным порядком символов"
    assert find_special_words([""]) == "", "Тест 2.8: Ошибка с пустыми словами"
    
    print("\n3. Тестирование find_symmetric...")
    assert find_symmetric(["radar", "hello", "12321"]) == ["radar", "12321"], "Тест 3.1: Ошибка поиска симметричных слов"
    assert find_symmetric(["level", "madam", "pop"]) == ["level", "madam", "pop"], "Тест 3.2: Ошибка с палиндромами"
    assert find_symmetric(["hello", "world"]) == [], "Тест 3.3: Ошибка: найдены несимметричные слова"
    assert find_symmetric([]) == [], "Тест 3.4: Ошибка с пустым списком"
    assert find_symmetric(["a", "bb", "ccc", "dddd"]) == ["a", "bb", "ccc", "dddd"], "Тест 3.5: Ошибка с односимвольными словами"
    assert find_symmetric(["1234321", "abcba", "12321"]) == ["1234321", "abcba", "12321"], "Тест 3.6: Ошибка с числовыми палиндромами"
    assert find_symmetric(["racecar", "deified", "rotator"]) == ["racecar", "deified", "rotator"], "Тест 3.7: Ошибка со сложными палиндромами"
    assert find_symmetric(["not", "palindrome", "test"]) == [], "Тест 3.8: Ошибка с непалиндромами"
    
    print("\n4. Тестирование find_max_num_in_symmetric...")
    assert find_max_num_in_symmetric(["aa", "11", "1a1", "12321", "abcba"]) == ["12321"], "Тест 4.1: Ошибка поиска слова с макс цифрами"
    assert find_max_num_in_symmetric(["123", "456", "789"]) == ["123", "456", "789"], "Тест 4.2: Ошибка с одинаковым количеством цифр"
    assert find_max_num_in_symmetric(["abc", "def", "ghi"]) == [], "Тест 4.3: Ошибка: найдены слова без цифр"
    assert find_max_num_in_symmetric(["1a1", "2b2", "3c3"]) == ["1a1", "2b2", "3c3"], "Тест 4.4: Ошибка с одинаковым количеством цифр в смешанных словах"
    assert find_max_num_in_symmetric(["12345", "12", "123", "1234"]) == ["12345"], "Тест 4.5: Ошибка с разным количеством цифр"
    assert find_max_num_in_symmetric(["1", "22", "333"]) == ["333"], "Тест 4.6: Ошибка с возрастающим количеством цифр"
    assert find_max_num_in_symmetric(["a1a", "b22b", "c333c"]) == ["c333c"], "Тест 4.7: Ошибка с цифрами внутри палиндромов"
    assert find_max_num_in_symmetric(["123454321", "12321", "1234321"]) == ["123454321"], "Тест 4.8: Ошибка с большими числовыми палиндромами"
