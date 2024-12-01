# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2019/day/1

from ...base import StrSplitSolution, answer


def fuel(mass: int) -> int:
    return mass // 3 - 2


def complex_fuel(mass: int) -> int:
    return 0 if fuel(mass) <= 0 else fuel(mass) + complex_fuel(fuel(mass))


class Solution(StrSplitSolution):
    _year = 2019
    _day = 1

    @answer(3376997)
    def part_1(self) -> int:
        return sum(fuel(int(line)) for line in self.input)

    @answer(5062623)
    def part_2(self) -> int:
        return sum(complex_fuel(int(line)) for line in self.input)
