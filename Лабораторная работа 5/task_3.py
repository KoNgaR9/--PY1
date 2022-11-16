import random

def get_unique_list_numbers() -> list[int]:
    unique_numbers = set(range(-10, 11))
    list_unique_numbers = [n for n in unique_numbers]
    random.shuffle(list_unique_numbers)
    return list_unique_numbers[:15]

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
