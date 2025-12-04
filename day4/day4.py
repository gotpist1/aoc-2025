from utils.input_utils import read_input, parse_input, InputGrid

class Response:
    def __init__(self, removed_rolls: int, input_grid: InputGrid):
        self.removed_rolls = removed_rolls
        self.input_grid = input_grid

def get_valid_positions(input_grid) -> Response:
    valid_positions = []
    for (y, x), value in input_grid.grid_dict.items():
        if value == '@':
            count = 0
            for dy, dx in input_grid.positions:
                ny, nx = y + dy, x + dx
                if (ny, nx) in input_grid.grid_dict and input_grid.grid_dict[(ny, nx)] == '@':
                    count += 1
            if count < 4:
                valid_positions.append((y, x))
    for rp in valid_positions:
        input_grid.grid_dict[rp] = '.'

    return Response(len(valid_positions), input_grid)

def part1(data):
    """Solve part 1 of the puzzle."""
    lines = parse_input(data)
    input_grid = InputGrid(lines)
    response = get_valid_positions(input_grid)

    return response.removed_rolls


def part2(data):
    """Solve part 2 of the puzzle."""
    lines = parse_input(data)
    total_removed_rolls = 0
    input_grid = InputGrid(lines)
    response = get_valid_positions(input_grid)
    while True:
        if response.removed_rolls == 0:
            break
        total_removed_rolls += response.removed_rolls
        input_grid = response.input_grid
        response = get_valid_positions(input_grid)
    return total_removed_rolls


def main():
    data = read_input()
    
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
