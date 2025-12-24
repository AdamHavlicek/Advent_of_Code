import os
import pprint


def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.read()

def parse_lines(lines):
    return [list(line) for line in lines.splitlines()]

def get_count_of_paper_rolls(lines, line_index, char_index):
    segment_lines = [
        int(char_ == '@')
        for slice_line in lines[line_index - int(line_index > 0):line_index + 2]
        for char_ in slice_line[char_index - int(char_index > 0):char_index + 2]
    ]

    return sum(segment_lines)

def process_lines(lines):
    paper_roll_char = '@'

    accessible_tiles = 0

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char != paper_roll_char:
                continue

            lines[line_index][char_index] = 'x'

            paper_rolls = get_count_of_paper_rolls(
                lines,
                line_index,
                char_index
            )
            if 0 <= paper_rolls < 4:
                accessible_tiles += 1

            lines[line_index][char_index] = char

    return accessible_tiles

def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_real.txt',
    )

    lines = read_lines(file_path)
    lines = parse_lines(lines)

    print(process_lines(lines))

if __name__ == '__main__':
    main()
    exit(0)
