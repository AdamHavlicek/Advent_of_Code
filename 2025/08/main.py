import os
import math
import itertools
import collections


def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.read()


def parse_lines(lines):
    return [tuple(map(int, line.split(','))) for line in lines.splitlines()]


def get_distance_between_points_v3(point, other_point):
    return math.dist(point, other_point)


def get_mul_of_connections(connection_list):
    largest_connections = sorted(connection_list, key=len)[::-1][:3]

    return math.prod(map(len, largest_connections))


def get_shortest_distances(coordinates, size):
    distances = {}

    for coord_combination in itertools.combinations(coordinates, 2):
        distances[coord_combination] = get_distance_between_points_v3(*coord_combination)

    return collections.OrderedDict(
        sorted(
            distances.items(),
            key=lambda kv: kv[1]
        )[:size]
    )


def process_lines(coordinates):
    distances = get_shortest_distances(coordinates, 1000)

    connection_list = []
    for coordinates, _ in distances.items():
        updated = False

        for connection in connection_list:
            if connection.isdisjoint(coordinates):
                continue

            connection.update(coordinates)
            updated = True
            break

        if not updated:
            connection_list.append(set(coordinates))

    # flaky AF
    for _ in range(50):
        new_connections_list = []
        connection = connection_list.pop(0)
        for other in connection_list:
            if connection.isdisjoint(other):
                new_connections_list.append(other)
                continue

            connection.update(other)

        new_connections_list.append(connection)
        connection_list = new_connections_list

    return get_mul_of_connections(connection_list)

def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_real.txt',
    )

    # MF!
    # 162,817,812;425,690,689;431,825,988;346,949,466;
    # 906,360,560;805,96,715;739,650,466;984,92,344;862,61,35;
    # 52,470,668;117,168,530;
    # 819,987,18;941,993,340;

    lines = read_lines(file_path)
    coordinates = parse_lines(lines)

    print(process_lines(coordinates))


if __name__ == '__main__':
    main()
    exit(0)
