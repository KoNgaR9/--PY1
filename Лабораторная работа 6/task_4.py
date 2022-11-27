import json

INPUT_FILE = "input.csv"

def csv_to_list_dict(csv_file) -> list[dict]:
    csv_data = []
    with open(csv_file) as f:
        for line in f:
            csv_data += [line.rstrip().split(",")]
    headlines = csv_data[:1][0]
    rows = csv_data[1:]

    list_dict = []
    dict_to_append = {}
    for row in rows:
        for index in range(len(row)):
            dict_to_append[headlines[index]] = row[index]
        list_dict.append(dict_to_append.copy())

    return list_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
