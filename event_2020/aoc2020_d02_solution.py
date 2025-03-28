# Advent of Code 2020 Day 2
# Password Philosophy
# https://adventofcode.com/2020/day/2

import re
import sys

VALID_CHK1 = lambda min_, max_, char, pword: min_ <= pword.count(char) <= max_
VALID_CHK2 = lambda p1, p2, char, pwrd: (pwrd[p1 - 1] == char) ^ (pwrd[p2 - 1] == char)


def parse(row: str) -> tuple[int, int, str, str]:
    pattern = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"
    match = re.match(pattern, row)
    if match:
        return int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)
    raise ValueError("No match in row")


def valid_count(input: list[str], valid_check) -> int:
    return sum(
        valid_check(a, b, char, pword)
        for row in input
        for a, b, char, pword in [parse(row)]
    )


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")

    part_1 = valid_count(input, VALID_CHK1)
    part_2 = valid_count(input, VALID_CHK2)

    print("Part 1:", part_1)  # 620
    print("Part 2:", part_2)  # 727
