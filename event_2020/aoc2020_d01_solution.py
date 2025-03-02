# Advent of Code 2020 Day 1
# Report Repair
# https://adventofcode.com/2020/day/1

import sys
from itertools import combinations
from math import prod


def solve(input: str, num_factors: int) -> int:
    parsed = [int(line) for line in input.split()]
    return next(
        prod(factors)
        for factors in combinations(parsed, num_factors)
        if sum(factors) == 2020
    )


if __name__ == "__main__":
    input: str = sys.stdin.read()

    part_1 = solve(input, 2)
    part_2 = solve(input, 3)

    print("Part 1:", part_1)  # 100419
    print("Part 2:", part_2)  # 265253940
