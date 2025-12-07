import re

class ReversedColumnParser:
    def __init__(self, data):
        self.data = data
        self.columns = self.parse_input_as_columns_keep_padding()


    def parse_input_as_columns_keep_padding(self):
        lines = self.data.split('\n')
        max_len = max(len(line) for line in lines)
        char_columns = []
        for col_idx in range(max_len):
            column = []
            for line in lines:
                if col_idx < len(line):
                    column.append(line[col_idx])
                else:
                    column.append(' ')
            char_columns.append(column)
        char_columns.reverse()
        problems = []
        current_problem = []

        for col in char_columns:
            if all(c == ' ' for c in col):
                if current_problem:
                    problems.append(current_problem)
                    current_problem = []
            else:
                current_problem.append(col)

        if current_problem:
            problems.append(current_problem)

        return self.convert_problems_to_numbers_and_operator_tuple(problems)

    @staticmethod
    def convert_problems_to_numbers_and_operator_tuple(problems):
        result = []
        for problem in problems:
            numbers = []
            operator = None

            for column in problem:
                digits = []
                for char in column:
                    if char.isdigit():
                        digits.append(char)
                    elif char in '*+':
                        operator = char
                if digits:
                    number = int(''.join(digits))
                    numbers.append(number)

            result.append((numbers, operator))

        return result
