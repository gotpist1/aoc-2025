from utils.input_utils import read_input, parse_input


def get_best_batteries(battery_bank, needed):
    result = []
    remaining_needed = needed
    start_index = 0

    while remaining_needed > 0:
        must_leave = remaining_needed - 1
        last_pickable = len(battery_bank) - must_leave - 1
        highest_pick = max(battery_bank[start_index:last_pickable + 1])
        position_to_pick_from = battery_bank.index(highest_pick, start_index)

        result.append(highest_pick)
        remaining_needed -= 1
        start_index = position_to_pick_from + 1

    return result

def part1(data):
    """Solve part 1 of the puzzle."""
    batteries = []
    lines = parse_input(data)
    for battery_bank in lines:
        batteries.append(int("".join(get_best_batteries(battery_bank, 2))))
    return sum(batteries)


def part2(data):
    """Solve part 2 of the puzzle."""
    battery_banks = parse_input(data)
    max_chunks = []
    for battery_bank in battery_banks:
        max_chunks.append(int(''.join(get_best_batteries(battery_bank, 12))))
    return sum(max_chunks)


def main():
    data = read_input("example.txt")
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
