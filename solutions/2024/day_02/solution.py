# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/2

from ...base import StrSplitSolution, answer


def parse(input: list[str]) -> list[list[int]]:
    return [list(map(int, line.split())) for line in input]


def is_safe(report: list[int]) -> bool:
    gaps = [abs(x - y) for x, y in zip(report, report[1:])]
    is_ordered = report in [sorted(report), sorted(report, reverse=True)]
    return is_ordered and all(1 <= gap <= 3 for gap in gaps)


def is_safe_dampened(report: list[int]) -> bool:
    dampened = [report[:level] + report[level + 1 :] for level in range(len(report))]
    return is_safe(report) or any(is_safe(dampened_rprt) for dampened_rprt in dampened)


class Solution(StrSplitSolution):
    _year = 2024
    _day = 2

    @answer(585)
    def part_1(self) -> int:
        return sum(1 for report in parse(self.input) if is_safe(report))

    @answer(626)
    def part_2(self) -> int:
        return sum(1 for report in parse(self.input) if is_safe_dampened(report))
