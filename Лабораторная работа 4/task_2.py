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
   
def percent_char(count_char_dict):
    i = 0
    percent_dict = {}
    for char in count_char_dict:
        i += count_char_dict.get(char)
    for char in count_char_dict:
        percent_dict[char] = round((count_char_dict.get(char)/i)*100, 2)
    check = 0
    for char in percent_dict:
        check += percent_dict.get(char)
    return percent_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
