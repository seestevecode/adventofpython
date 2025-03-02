# Advent of Code 2021 Day 1
# Sonar Sweep
# https://adventofcode.com/2021/day/1

import sys


def solve(input: str, offset: int) -> int:
    parsed = [int(line) for line in input.split()]
    return sum(num2 > num1 for num1, num2 in zip(parsed, parsed[offset:]))


if __name__ == "__main__":
    input: str = sys.stdin.read()

    part_1 = solve(input, 1)
    part_2 = solve(input, 3)

    print("Part 1:", part_1)  # 1759
    print("Part 2:", part_2)  # 1805
