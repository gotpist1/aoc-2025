def read_input(filename='input.txt'):
    """Read and return the input file content."""
    with open(filename, 'r') as f:
        return f.read().strip()


def parse_input(data, separator='\n'):
    """Parse the input data into a usable format."""
    lines = data.split(separator)
    return lines

class InputGrid:
    def __init__(self, input_data):
        self.data = input_data
        self.height = len(input_data)
        self.width = len(input_data[0])
        self.grid_dict = {(y, x): input_data[y][x] for y in range(self.height) for x in range(self.width)}
        self.positions = [(py, px) for py in [-1, 0, 1] for px in [-1, 0, 1] if (px != 0 or py != 0)]