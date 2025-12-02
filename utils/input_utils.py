def read_input(filename='input.txt'):
    """Read and return the input file content."""
    with open(filename, 'r') as f:
        return f.read().strip()


def parse_input(data, separator='\n'):
    """Parse the input data into a usable format."""
    lines = data.split(separator)
    return lines