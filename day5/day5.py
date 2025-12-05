from utils.input_utils import read_input
from database import Database


def part1(data):
    """Solve part 1 of the puzzle."""
    is_fresh = 0
    database = Database(data)
    for ingredient_id in database.ingredients:
        for id_range in database.ranges_list:
            if id_range[0] <= ingredient_id <= id_range[1]:
                is_fresh += 1
    return is_fresh


def part2(data):
    """Solve part 2 of the puzzle."""
    database = Database(data)
    return sum(end - start + 1 for start, end in database.ranges_list)


def main():
    data = read_input()
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
