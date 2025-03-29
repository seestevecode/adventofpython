# Advent of Code 2019 Day 1
# The Tyranny of the Rocket Equation
# https://adventofcode.com/2019/day/1

import sys


def fuel(mass: int, recurse: bool = False) -> int:
    base = mass // 3 - 2
    return base if not recurse else 0 if base <= 0 else base + fuel(base, recurse=True)


if __name__ == "__main__":
    input: str = sys.stdin.read()
    parsed = [int(line) for line in input.split()]

    part_1: int = sum(fuel(mass) for mass in parsed)
    part_2: int = sum(fuel(mass, recurse=True) for mass in parsed)

    print("Part 1:", part_1)  # 3376997
    print("Part 2:", part_2)  # 5062623
