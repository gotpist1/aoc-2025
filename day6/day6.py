from utils.column_parser import ReversedColumnParser
from utils.input_utils import read_input, parse_input_as_columns


class MathProblem:
    def __init__(self, problem_data):
        self.data = problem_data
        self.values = self.parse_values()
        self.operator = self.data[-1]

    def parse_values(self):
        values = [int(x.strip()) for x in self.data[0: len(self.data) - 1]]
        return values


def part1(data):
    """Solve part 1 of the puzzle."""
    results = []
    math_problems = [MathProblem(line) for line in parse_input_as_columns(data)]
    for mp in math_problems:
        result = 0
        if mp.operator == "+":
            result = sum(mp.values)
        elif mp.operator == "*":
            result = 1
            for v in mp.values:
                result *= v
        results.append(result)

    return sum(results)


def part2(data):
    """Solve part 2 of the puzzle."""
    results = []
    problems = ReversedColumnParser(data).columns
    for numbers, operator in problems:
        result = 0
        if operator == "+":
            result = sum(numbers)
        elif operator == "*":
            result = 1
            for v in numbers:
                result *= v
        results.append(result)

    return sum(results)


def main():
    data = read_input(no_strip=True)
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
