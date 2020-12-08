from days.day import Day
from itertools import combinations


class Day01(Day):
    def __init__(self):
        super().__init__()
        self.lines = [int(line) for line in self.lines]

        self.target_sum = self.args.target_sum

    def add_extra_args(self):
        self.parser.add_argument(
            '--target-sum', type=int, default=2020, help="Target sum to reach")

    def multiple_of_found_sum(self, number_of_elements_to_sum):
        result = 1
        for items in combinations(self.lines, number_of_elements_to_sum):
            if sum(items) == self.target_sum:
                for item in items:
                    result *= item
                break
        return result

    def part1(self):
        return self.multiple_of_found_sum(2)

    def part2(self):
        return self.multiple_of_found_sum(3)