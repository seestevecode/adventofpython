# Advent of Code 2020 Day 2
# Password Philosophy
# https://adventofcode.com/2020/day/2

import re
import sys

COUNT_IN_RANGE = lambda low, high, char, pwd: low <= pwd.count(char) <= high
CHAR_IN_POSITION = lambda a, b, char, pwd: (pwd[a - 1] == char) ^ (pwd[b - 1] == char)


def parse(row: str) -> tuple[int, int, str, str]:
    if match := re.match(r"(\d+)-(\d+) ([a-z]): ([a-z]+)", row):
        return int(match.group(1)), int(match.group(2)), match.group(3), match.group(4)
    raise ValueError("No match in row")


def valid_count(input: list[str], valid_check) -> int:
    return sum(valid_check(*parse(row)) for row in input)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")

    part_1: int = valid_count(input, COUNT_IN_RANGE)
    part_2: int = valid_count(input, CHAR_IN_POSITION)

    print("Part 1:", part_1)  # 620
    print("Part 2:", part_2)  # 727
