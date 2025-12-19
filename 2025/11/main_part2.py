import os
from functools import cache


def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.readlines()


def parse_lines(lines):
    nodes = {}

    for line in lines:
        formatted_line = line.replace("\n", "")
        key_, unparsed_nodes = formatted_line.split(": ")
        nodes[key_] = unparsed_nodes.split(" ")

    return nodes


def find_all_paths(graph, start, end):

    @cache
    def process_node(current, already_in_dac, already_in_fft):
        if current == end:
            return int(already_in_dac and already_in_fft)

        node_list = graph[current]
        return sum(
            process_node(
                node_,
                already_in_dac or current == 'dac',
                already_in_fft or current == 'fft',
            )
            for node_ in node_list
        )

    return process_node(start, False, False)


if __name__ == '__main__':
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input_part2.txt',
        'input_part2_real.txt',
    )

    lines = read_lines(file_path)

    parsed_nodes = parse_lines(lines)

    result = find_all_paths(
        parsed_nodes,
        "svr",
        "out",
    )
    print(result)

    exit(0)
