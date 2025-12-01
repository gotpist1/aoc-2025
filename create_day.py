#!/usr/bin/env python3
"""
Template generator for Advent of Code days.
Usage: python create_day.py <day_number>
"""
import os
import sys


TEMPLATE = '''from utils.input_utils import read_input, parse_input


def part1(data):
    """Solve part 1 of the puzzle."""
    lines = parse_input(data)
    # TODO: Implement part 1 solution
    return 0


def part2(data):
    """Solve part 2 of the puzzle."""
    lines = parse_input(data)
    # TODO: Implement part 2 solution
    return 0


def main():
    data = read_input()
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
'''


def create_day(day_num):
    """Create a new day folder with template files."""
    folder_name = f"day{day_num}"

    if os.path.exists(folder_name):
        print(f"Error: {folder_name} already exists!")
        return

    os.makedirs(folder_name)

    # Create Python file
    with open(os.path.join(folder_name, f"day{day_num}.py"), 'w') as f:
        f.write(TEMPLATE)

    # Create input files
    with open(os.path.join(folder_name, "input.txt"), 'w') as f:
        f.write(f"# Paste your Advent of Code Day {day_num} input here\n")

    with open(os.path.join(folder_name, "example.txt"), 'w') as f:
        f.write("# Paste example input from the problem here\n")

    print(f"Created {folder_name}/ with day{day_num}.py, input.txt, and example.txt")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_day.py <day_number>")
        sys.exit(1)

    try:
        day = int(sys.argv[1])
        if day < 1 or day > 25:
            print("Day number must be between 1 and 25")
            sys.exit(1)
        create_day(day)
    except ValueError:
        print("Day number must be an integer")
        sys.exit(1)


