from utils.input_utils import read_input, parse_input, InputGrid


def part1(data):
    """Solve part 1 of the puzzle."""
    lines = parse_input(data)
    grid = InputGrid(lines)
    y, x = next(k for k, v in grid.grid_dict.items() if v == 'S')
    beams = [(y, x)]
    split_count = 0
    visited = set()
    while beams:
        cy, cx = beams.pop()
        ny = cy + 1
        if ny >= len(lines):
            continue

        if cx < 0 or cx >= len(lines[ny]):
            continue

        if (ny, cx) in visited:
            continue
        visited.add((ny, cx))

        if grid.grid_dict.get((ny, cx)) == '^':
            split_count += 1
            beams.append((ny, cx - 1))
            beams.append((ny, cx + 1))
        else:
            beams.append((ny, cx))
    return split_count


def part2(data):
    """Solve part 2 of the puzzle."""
    lines = parse_input(data)
    grid = InputGrid(lines)

    y, x = next(k for k, v in grid.grid_dict.items() if v == 'S')
    memo = {}

    def count_timelines(cy, cx):
        if (cy, cx) in memo:
            return memo[(cy, cx)]

        ny = cy + 1

        if ny >= len(lines) or cx < 0 or cx >= len(lines[ny]):
            return 1

        if grid.grid_dict.get((ny, cx)) == '^':
            left_count = count_timelines(ny, cx - 1)
            right_count = count_timelines(ny, cx + 1)
            result = left_count + right_count
        else:
            result = count_timelines(ny, cx)

        memo[(cy, cx)] = result
        return result

    return count_timelines(y, x)


def main():
    data = read_input()
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
