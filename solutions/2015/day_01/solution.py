# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2015/day/1

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2015
    _day = 1

    @answer((280, 1797))
    def solve(self) -> tuple[int, int]:
        floor, steps = 0, 0
        for step, move in enumerate(self.input, start=1):
            floor += 1 if move == "(" else -1 if move == ")" else 0
            if floor == -1 and not steps:
                steps = step
        return floor, steps
