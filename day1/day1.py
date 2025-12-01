from utils.input_utils import read_input, parse_input

def count_zero_ticks(tick_instructions, rotation_start=50):
    """Count the number of ticks with value zero after applying instructions."""
    ticks = []
    for instruction in tick_instructions:
        operator = instruction[0]
        value = int(instruction[1:])
        if operator == 'L':
            rotation_start = (rotation_start - value) % 100
        else:
            rotation_start = (rotation_start + value) % 100
        if rotation_start == 0:
            ticks.append(rotation_start)
    return ticks.count(0)


def count_zero_ticks_all_occurances(tick_instructions, rotation_start=50):
    """Count the number of ticks with value zero after applying instructions, considering all occurrences."""
    ticks = []
    for instruction in tick_instructions:
        operator = instruction[0]
        value = int(instruction[1:])
        if operator == 'L':
            for _ in range(value):
                rotation_start = (rotation_start - 1) % 100
                if rotation_start == 0:
                    ticks.append(rotation_start)
        else:
            for _ in range(value):
                rotation_start = (rotation_start + 1) % 100
                if rotation_start == 0:
                    ticks.append(rotation_start)
    return ticks.count(0)




def part1(data):
    """Solve part 1 of the puzzle."""
    lines = parse_input(data)
    t = count_zero_ticks(lines)
    return t


def part2(data):
    """Solve part 2 of the puzzle."""
    lines = parse_input(data)
    t = count_zero_ticks_all_occurances(lines)
    return t


def main():
    data = read_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()

