from utils.input_utils import parse_input

class Database:
    def __init__(self, data):
        self.database_raw = parse_input(data,  separator='\n\n')
        self.ranges = parse_input(self.database_raw[0])
        self.ingredients = [int(x) for x in parse_input(self.database_raw[1])]
        self.ranges_list = self.parse_ranges()
        self.flattened_ranges = [id_range for sublist in self.ranges_list for id_range in sublist]

    def parse_ranges(self) -> list[list[int]]:
        ranges_list = []
        for range_str in self.ranges:
            range_start, range_end = range_str.split('-')
            ranges_list.append([int(range_start), int(range_end)])

        return self.__merge_ranges(ranges_list)

    @staticmethod
    def __merge_ranges(ranges) -> list[list[int]]:
        ranges.sort(key=lambda x: x[0])
        merged = [ranges[0]]
        for current in ranges[1:]:
            last = merged[-1]
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)
        return merged