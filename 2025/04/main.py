import os

def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.read()

def parse_lines(lines):
    ranges = []
    id_list = []

    for line in lines.splitlines():
        if line == '':
            continue

        if line.isdigit():
            id_list.append(int(line))
        else:
            ranges.append(list(map(int, line.split('-'))))

    return ranges, id_list

def sum_of_valid_ids(ranges, id_):
    for range_start, range_end in ranges:
        if range_start <= id_ <= range_end:
            return 1

    return 0

def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_real.txt',
    )

    lines = read_lines(file_path)

    ranges_with_id_list = parse_lines(lines)

    result = sum(map(
        lambda id_: sum_of_valid_ids(ranges_with_id_list[0], id_),
        ranges_with_id_list[1],
    ))

    print(result)

if __name__ == '__main__':
    main()
    exit(0)
