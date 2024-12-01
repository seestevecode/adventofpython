# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2017/day/1

from ...base import TextSolution, answer


def captcha(seq: str, off: int) -> int:
    return sum(int(n) for i, n in enumerate(seq) if seq[i] == seq[(i + off) % len(seq)])


class Solution(TextSolution):
    _year = 2017
    _day = 1

    @answer((1390, 1232))
    def solve(self) -> tuple[int, int]:
        return captcha(self.input, 1), captcha(self.input, len(self.input) // 2)
