def get_count_char(str_):
    total = {}
    str_ = str_.lower()

    for char in str_:
        if not char.isalpha():
            continue

        if char not in total:
            total[char] = 1
        else:
            total[char] += 1
    return total
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
