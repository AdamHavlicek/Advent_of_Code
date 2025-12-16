import os
import pprint

def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.readlines()

def parse_lines(lines):
    nodes = {}

    for line in lines:
        formatted_line = line.replace("\n", "")
        split_line = formatted_line.split(" ")
        nodes[split_line[0].replace(":", "")] = split_line[1:]

    return nodes

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths

if __name__ == '__main__':
    file_path = os.path.join(
        os.path.dirname(__file__),
        'input_real.txt',
    )

    lines = read_lines(file_path)

    parsed_nodes = parse_lines(lines)

    all_found_paths = find_all_paths(parsed_nodes, "you", "out")

    print(len(all_found_paths))

    exit(0)