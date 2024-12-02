# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2020/day/1


from itertools import combinations
from math import prod

from ...base import StrSplitSolution, answer


def find_combo(input: list[str], combo_size: int) -> int:
    for combo in combinations([int(num) for num in input], combo_size):
        if sum(combo) == 2020:
            return prod(combo)
    raise ValueError("You didn't find the right combo")


class Solution(StrSplitSolution):
    _year = 2020
    _day = 1

    @answer((100419, 265253940))
    def solve(self) -> tuple[int, int]:
        return find_combo(self.input, 2), find_combo(self.input, 3)
