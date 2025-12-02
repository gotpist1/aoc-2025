from utils.input_utils import read_input, parse_input

def is_duplicate_sequence(number):
    num_as_str = str(number)
    if len(num_as_str) % 2 != 0:
        return False
    mid = len(num_as_str) // 2
    left_half = num_as_str[:mid]
    right_half = num_as_str[mid:]

    return left_half == right_half

def is_repeated_sequence(number):
    num_str = str(number)
    length = len(num_str)

    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:
            pattern = num_str[:pattern_length]
            if pattern * (length // pattern_length) == num_str:
                return True

    return False

def find_dublicate_ids_in_list(ids):
    duplicates = set()
    for id_range in ids:
        for id in range(id_range[0], id_range[1] + 1):
            if is_duplicate_sequence(id):
                duplicates.add(id)

    return sum(list(duplicates))


def find_repeated_pattern_ids_in_list(ids):
    repeated = set()
    for id_range in ids:
        for id in range(id_range[0], id_range[1] + 1):
            if is_repeated_sequence(id):
                repeated.add(id)

    return sum(list(repeated))


def part1(data):
    """Solve part 1 of the puzzle."""
    lines = parse_input(data, separator=',')
    id_ranges = [[int(x) for x in item.split('-')] for item in lines]
    return find_dublicate_ids_in_list(id_ranges)


def part2(data):
    """Solve part 2 of the puzzle."""
    lines = parse_input(data, separator=',')
    id_ranges = [[int(x) for x in item.split('-')] for item in lines]
    return find_repeated_pattern_ids_in_list(id_ranges)


def main():
    data = read_input()

    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
