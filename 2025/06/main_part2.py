import io
import pathlib
import os
from functools import reduce


def load_file(path: pathlib.Path) -> io.StringIO:
    with open(path, 'r') as opened_file:
        return io.StringIO(opened_file.read())

def get_operators_with_padding(line: str):
    result = []

    operator = line[0]
    padding = 0
    allowed_operators = ['+', '*']
    for char in line[1:]:
        if char not in allowed_operators:
            padding += 1
            continue

        result.append({
            'operator': operator,
            'padding': padding
        })
        operator = char
        padding = 0

    result.append({'operator': operator, 'padding': padding})

    return result

def parse_number_line(column_list: list[dict], line: str):
    cursor = 0
    empty_space_size = 1
    for column in column_list:
        if column.get('values') is None:
            column['values'] = []

        number_string = line[cursor:cursor + column['padding']]
        column['values'].append(number_string)
        cursor += column['padding'] + empty_space_size

def parse_lines(column_list: list[dict], lines: list[str]):
    for line in lines:
        parse_number_line(column_list, line)

def get_values(value_list: list[str], padding: int):
    result_values = []

    for char_index in reversed(range(0, padding)):
        number_string = ''
        for value_index in range(0, len(value_list)):
            number_string += value_list[value_index][char_index]

        result_values.append(int(number_string))

    return result_values


def total_sum(column_list):
    result = 0

    for column in column_list:
        int_values = get_values(column['values'], column['padding'])

        operation_fn = lambda num, other: num + other
        if column['operator'] == '*':
            operation_fn = lambda num, other: num * other

        result += reduce(operation_fn, int_values)


    return result


if __name__ == "__main__": 
    file_path = os.path.join(os.path.dirname(__file__), "input_part2_real.txt")

    contents = load_file(file_path)
    lines = contents.readlines()

    operators_with_padding = get_operators_with_padding(lines[-1])
    parse_lines(operators_with_padding, lines[:-1])

    print(total_sum(reversed(operators_with_padding)))

    exit()