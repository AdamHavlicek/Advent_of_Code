import collections
import itertools
import math
import os

def read_lines(path):
    with open(path, 'r') as opened_file:
        return opened_file.read()


def parse_lines(lines):
    return [
        tuple(map(int, line.split(',')))
        for line in lines.splitlines()
    ]

class Rect:
    def __init__(self, point, other_point):
        self.point = point
        self.other_point = other_point

    def __str__(self):
        return f'Rect({self.point}, {self.other_point})'

    def distance(self):
        return math.dist(self.point, self.other_point)

    def width(self):
        max_y = max(self.point[1], self.other_point[1])
        min_y = min(self.point[1], self.other_point[1])

        return (max_y - min_y) + 1

    def height(self):
        max_x = max(self.point[0], self.other_point[0])
        min_x = min(self.point[0], self.other_point[0])

        return (max_x - min_x) + 1

    def area(self):
        return self.width() * self.height()

def process_points(points):
    points = sorted(points)

    rect = None
    for point, other_point in itertools.combinations(points, 2):
        if not rect or rect.area() < Rect(point, other_point).area():
            rect = Rect(point, other_point)

    return rect.area()

def main():
    file_path = os.path.join(
        os.path.dirname(__file__),
        # 'input.txt',
        'input_real.txt',
    )

    lines = read_lines(file_path)
    points = parse_lines(lines)

    print(process_points(points))


if __name__ == '__main__':
    main()
    exit(0)
