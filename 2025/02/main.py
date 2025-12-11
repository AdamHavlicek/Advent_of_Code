import os

def load_file(path) -> str:
    with open(path, 'r') as opened_file:
        return opened_file.read()

def get_range_list(raw_string: str):
    range_list = raw_string.split(",")
    return [list(map(int, range_.split('-'))) for range_ in range_list]

def is_valid(id_number: int):
    id_str = str(id_number)
    if id_str[len(id_str) // 2:][0] == '0':
        return True

    is_duplicit = id_str[0: len(id_str) // 2] == id_str[len(id_str) // 2 :]

    return not is_duplicit

def get_sum_of_invalid_ids(range_list: list[list[int]]):
    invalid_ids = []

    for range_ in range_list:
        for id_number in range(range_[0], range_[1] + 1):
            if not is_valid(id_number):
                invalid_ids.append(id_number)

    return sum(invalid_ids)


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input_real.txt")

    contents = load_file(file_path)

    parsed_range_list = get_range_list(contents)

    print(get_sum_of_invalid_ids(parsed_range_list))

    exit(0)
