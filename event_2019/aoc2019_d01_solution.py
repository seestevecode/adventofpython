# Advent of Code 2019 Day 1
# The Tyranny of the Rocket Equation
# https://adventofcode.com/2019/day/1

import sys


def parse(input: str) -> list[int]:
    return [int(line) for line in input.split()]


def fuel(mass: int, recurse: bool = False) -> int:
    base = mass // 3 - 2
    return base if not recurse else 0 if base <= 0 else base + fuel(base, recurse=True)


def part_1(input: str) -> int:
    return sum(fuel(mass) for mass in parse(input))


def part_2(input: str) -> int:
    return sum(fuel(mass, recurse=True) for mass in parse(input))


if __name__ == "__main__":
    input: str = sys.stdin.read()

    print("Part 1:", part_1(input))  # 3376997
    print("Part 2:", part_2(input))  # 5062623
