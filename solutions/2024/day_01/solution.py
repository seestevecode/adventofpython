# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/1

from ...base import StrSplitSolution, answer


def parse(input: list[str]) -> list[list[int]]:
    """Return a list of (two) sorted lists"""
    parsed_lines = [map(int, line.split()) for line in input]
    return [sorted(list_of_nums) for list_of_nums in zip(*parsed_lines)]


class Solution(StrSplitSolution):
    _year = 2024
    _day = 1

    @answer(3714264)
    def part_1(self) -> int:
        list_of_pairs = [tuple(x) for x in zip(*parse(self.input))]
        return sum(abs(pair[0] - pair[1]) for pair in list_of_pairs)

    @answer(18805872)
    def part_2(self) -> int:
        left, right = parse(self.input)
        return sum(num * right.count(num) for num in left)
