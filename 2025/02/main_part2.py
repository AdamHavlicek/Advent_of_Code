import os
import pprint
from functools import reduce


def load_file(path) -> str:
    with open(path, 'r') as opened_file:
        return opened_file.read()

def get_range_list(raw_string: str):
    range_list = raw_string.split(",")
    return [list(map(int, range_.split('-'))) for range_ in range_list]

def is_invalid(id_number: int):
    id_str = str(id_number)

    if id_str[len(id_str) // 2:][0] == '0':
        return False

    allowed_chunks = []
    for chunk_size in range(1, len(id_str) // 2 + 1):
        allowed_chunks.append(chunk_size)

    for chunk_size in reversed(allowed_chunks):
        chunks = []

        cursor = 0
        while cursor < len(id_str):
            chunks.append(id_str[cursor:cursor+chunk_size])
            cursor += chunk_size

        chunks_invalid = len(set(chunks)) == 1
        if chunks_invalid:
            return True

    return False

def get_sum_of_invalid_ids(range_list: list[list[int]]):
    invalid_ids = []

    for range_ in range_list:
        for id_number in range(range_[0], range_[1] + 1):
            if not is_invalid(id_number):
                continue

            invalid_ids.append(id_number)

    pprint.pprint(sorted(invalid_ids))
    return sum(invalid_ids)


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), "input_part2_real.txt")

    contents = load_file(file_path)

    parsed_range_list = get_range_list(contents)

    result_sum = get_sum_of_invalid_ids(parsed_range_list)
    print(result_sum)

    exit(0)
