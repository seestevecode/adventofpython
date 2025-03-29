# Advent of Code 2020 Day 1
# Report Repair
# https://adventofcode.com/2020/day/1

import sys
from itertools import combinations
from math import prod


def solve(factors: list[int], num_factors: int) -> int:
    return next(
        prod(factors)
        for factors in combinations(factors, num_factors)
        if sum(factors) == 2020
    )


if __name__ == "__main__":
    input: str = sys.stdin.read()
    parsed = [int(line) for line in input.split()]

    part_1: int = solve(parsed, 2)
    part_2: int = solve(parsed, 3)

    print("Part 1:", part_1)  # 100419
    print("Part 2:", part_2)  # 265253940
