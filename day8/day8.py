from utils.input_utils import read_input, parse_input
from utils.union_find import UnionFind
import math


def distance_3d(point1, point2):
    """Calculate the Euclidean distance between two 3D points."""
    return math.sqrt(
        (point1[0] - point2[0]) ** 2 +
        (point1[1] - point2[1]) ** 2 +
        (point1[2] - point2[2]) ** 2
    )

def get_distance_point_dict(junction_boxes):
    c = []
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            p1 = junction_boxes[i]
            p2 = junction_boxes[j]
            distance = distance_3d(junction_boxes[i], junction_boxes[j])
            c.append((distance, p1, p2))
    c.sort()
    return c

def part1(data):
    """Solve part 1 of the puzzle."""
    junction_boxes = [(int(x[0]), int(x[1]), int(x[2])) for line in parse_input(data) for x in [line.split(",")]]
    c = get_distance_point_dict(junction_boxes)
    uf = UnionFind()
    top_distances = c[:1000]

    for distance, p1, p2 in top_distances:
        uf.union(p1, p2)

    circuits = {}
    for distance, p1, p2 in top_distances:
        for point in [p1, p2]:
            root = uf.find(point)
            if root not in circuits:
                circuits[root] = []
            if point not in circuits[root]:
                circuits[root].append(point)
    result = 1
    for _, points in sorted(circuits.items(), key=lambda x: len(x[1]), reverse=True)[:3]:
        t = len(points)
        result *= t
        print(f"Circuit: {len(points)}")

    return result


def part2(data):
    """Solve part 2 of the puzzle."""
    junction_boxes = [(int(x[0]), int(x[1]), int(x[2])) for line in parse_input(data) for x in [line.split(",")]]
    distances = get_distance_point_dict(junction_boxes)
    uf = UnionFind()
    for distance, p1, p2 in distances:
        if uf.find(p1) != uf.find(p2):
            uf.union(p1, p2)
            roots = set(uf.find(point) for point in junction_boxes)
            if len(roots) == 1:
                print(f"Connecting edge: {p1} and {p2}")
                print(f"X coordinates: {p1[0]} and {p2[0]}")
                return p1[0] * p2[0]

    return 0

def main():
    data = read_input()
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
