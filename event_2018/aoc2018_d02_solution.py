# Advent of Code 2018 Day 2
# Inventory Management System
# https://adventofcode.com/2018/day/2

import itertools
import sys


def count_xs(input: list[str], target: int) -> int:
    return sum(target in {line.count(char) for char in set(line)} for line in input)


def part_1(input: list[str]) -> int:
    return count_xs(input, 2) * count_xs(input, 3)


def part_2(input: list[str]) -> str:
    results = []
    for line1, line2 in itertools.combinations(input, 2):
        assert len(line1) == len(line2)
        common = "".join(
            [char for pos, char in enumerate(line1) if line1[pos] == line2[pos]]
        )
        if len(common) == len(line1) - 1:
            results.append(common)
    assert len(results) == 1
    return results[0]


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    print("Part 1:", part_1(input))  # 7470
    print("Part 2:", part_2(input))  # kqzxdenujwcstybmgvyiofrrd
