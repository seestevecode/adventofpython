# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2024/day/3

import re

from ...base import TextSolution, answer


class Solution(TextSolution):
    _year = 2024
    _day = 3

    @answer(162813399)
    def part_1(self) -> int:
        hits = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.input)
        return sum(int(a) * int(b) for a, b in hits)

    @answer(53783319)
    def part_2(self) -> int:
        hits = re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)|don't\(\)|do\(\)", self.input)
        total, active = 0, True
        for hit in hits:
            command, num1, num2 = hit.group(0, 1, 2)
            if command == "do()":
                active = True
            elif command == "don't()":
                active = False
            elif active:
                total += int(num1) * int(num2)
            else:
                assert not active
        return total
