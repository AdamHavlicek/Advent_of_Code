import os
import pprint
from collections import defaultdict


def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.read()

def parse_lines(lines):
    return [list(line) for line in lines.splitlines()]

def process_lines(lines):
    allowed_characters = ['|', 'S']

    cache = defaultdict(int)
    cache[lines[0].index(allowed_characters[1])] = 1

    for line_index, line in enumerate(lines, 0):
        for char_index, char in enumerate(line):
            is_line_above = line_index - 1 >= 0 and lines[line_index - 1][ char_index] in allowed_characters
            if char == "^" and is_line_above:
                lines[line_index][char_index - 1] = "|"
                lines[line_index][char_index + 1] = "|"

                cache[char_index - 1] += cache[char_index]
                cache[char_index + 1] += cache[char_index]
                cache[char_index] = 0
                continue

            if is_line_above:
                lines[line_index][char_index] = "|"


    return sum(cache.values())

def display_lines(lines):
    pprint.pprint(["".join(line) for line in lines])

def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_real.txt',
    )

    lines = read_lines(file_path)
    lines = parse_lines(lines)

    print(process_lines(lines))
    display_lines(lines)

if __name__ == '__main__':
    main()
    exit(0)
