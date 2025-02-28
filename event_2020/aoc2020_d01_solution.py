# Advent of Code 2020 Day 1
# Report Repair
# https://adventofcode.com/2020/day/1

import sys
from itertools import combinations
from math import prod


def solve(input: str, num_factors: int) -> int:
    parsed = [int(line) for line in input.split()]
    products = [
        prod(factors)
        for factors in combinations(parsed, num_factors)
        if sum(factors) == 2020
    ]
    assert len(products) == 1, "There is more than one solution"
    return products[0]


def part_1(input: str) -> int:
    return solve(input, 2)


def part_2(input: str) -> int:
    return solve(input, 3)


if __name__ == "__main__":
    input: str = sys.stdin.read()

    print("Part 1:", part_1(input))  # 100419
    print("Part 2:", part_2(input))  # 265253940
