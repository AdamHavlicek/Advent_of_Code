import os


def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.readlines()

def process_line(line: str, number_of_digits: int):
    index_list = []

    for _ in range(number_of_digits):
        index_with_highest_digit = index_list[-1] + 1 if len(index_list) else 0

        stop_index = len(line) - number_of_digits + len(index_list) + 1
        for index in range(index_with_highest_digit, stop_index):
            is_not_bigger = int(line[index]) <= int(line[index_with_highest_digit])
            if is_not_bigger:
                continue

            index_with_highest_digit = index

        index_list.append(index_with_highest_digit)

    value_list = [line[index] for index in index_list]

    return int("".join(value_list))

def process_lines(instruction_list, number_of_digits: int):
    numbers = []

    for instruction in instruction_list:
        sanitized_instruction = instruction.replace("\n", "")
        numbers.append(process_line(sanitized_instruction, number_of_digits))

    return sum(numbers)

if __name__ == '__main__':
    file_path = os.path.join(
        os.path.dirname(__file__),
        'input_real.txt',
    )

    instructions = read_lines(file_path)

    print(process_lines(instructions, 2))

    exit(0)
