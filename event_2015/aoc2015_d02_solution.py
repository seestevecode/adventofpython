# Advent of Code 2015 Day 2
# I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2

import sys


def parse(input: list[str]) -> list[list[int]]:
    return [sorted(map(int, line.split("x"))) for line in input]


def part_1(input: list[str]) -> int:
    return sum(2 * (a * b + b * c + c * a) + a * b for a, b, c in parse(input))


def part_2(input: list[str]) -> int:
    return sum(2 * (a + b) + a * b * c for a, b, c in parse(input))


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    print("Part 1:", part_1(input))  # 1586300
    print("Part 2:", part_2(input))  # 3737498
