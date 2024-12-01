# Generate using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2018/day/1

from itertools import accumulate, cycle

from ...base import StrSplitSolution, answer


def parse(input):
    return [int(line) for line in input]


class Solution(StrSplitSolution):
    _year = 2018
    _day = 1

    @answer(508)
    def part_1(self) -> int:
        return sum(parse(self.input))

    @answer(549)
    def part_2(self) -> int:
        seen = set()
        for frequency in accumulate(cycle(parse(self.input))):
            if frequency in seen:
                return frequency
            seen.add(frequency)
        raise ValueError("You didn't reach the same frequency twice")
