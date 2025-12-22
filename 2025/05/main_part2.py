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

def merge_ranges(ranges):
    merged_ranges = [ranges[0]]

    for (range_start, range_end) in ranges[1:]:
        (last_merged_start, last_merged_end) = merged_ranges[-1]

        if range_start <= last_merged_end:
            merged_ranges[-1] = (last_merged_start, max(last_merged_end, range_end))
        else:
            merged_ranges.append((range_start, range_end))

    return merged_ranges

def count_valid_ids(ranges):
    count = 0

    for range_ in ranges:
        count += range_[1] - range_[0] + 1

    return count

def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_real.txt',
    )

    lines = read_lines(file_path)

    ranges_with_id_list = parse_lines(lines)

    result = count_valid_ids(
        merge_ranges(
            sorted(ranges_with_id_list[0])
        )
    )

    print(result)

if __name__ == '__main__':
    main()
    exit(0)
