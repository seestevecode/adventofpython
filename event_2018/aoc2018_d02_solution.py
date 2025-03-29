# Advent of Code 2018 Day 2
# Inventory Management System
# https://adventofcode.com/2018/day/2

import itertools
import sys


def count_xs(input: list[str], target: int) -> int:
    return sum(target in {line.count(char) for char in set(line)} for line in input)


def common_chars(line1: str, line2: str) -> str:
    return "".join(c for c1, c2, c in zip(line1, line2, line1) if c1 == c2)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    part_1: int = count_xs(input, 2) * count_xs(input, 3)
    part_2: str = next(
        common
        for line1, line2 in itertools.combinations(input, 2)
        if len(common := common_chars(line1, line2)) == len(line1) - 1
    )

    print("Part 1:", part_1)  # 7470
    print("Part 2:", part_2)  # kqzxdenujwcstybmgvyiofrrd
