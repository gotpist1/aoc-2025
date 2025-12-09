from utils.input_utils import read_input, parse_input
from utils.polygon_utils import PolygonHelper


def part1(data):
    """Solve part 1 of the puzzle."""
    coordinates = [(int(x), int(y)) for line in parse_input(data) for x, y in [line.split(",")]]
    max_area = 0
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]
            if x1 != x2 and y1 != y2:
                width = abs(x2 - x1) + 1
                height = abs(y2 - y1) + 1
                area = width * height
                max_area = max(max_area, area)
    return max_area


def part2(data):
    """Solve part 2 of the puzzle."""
    coordinates = [(int(x), int(y)) for line in parse_input(data) for x, y in [line.split(",")]]
    p_helper = PolygonHelper()
    n = len(coordinates)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = coordinates[i]
            x2, y2 = coordinates[j]

            if x1 == x2 or y1 == y2:
                continue

            left, right = min(x1, x2), max(x1, x2)
            top, bottom = min(y1, y2), max(y1, y2)

            if p_helper.is_rectangle_valid(left, right, top, bottom, coordinates):
                area = (right - left + 1) * (bottom - top + 1)
                max_area = max(max_area, area)

    return max_area


def main():
    data = read_input()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
