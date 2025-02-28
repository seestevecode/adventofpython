# Advent of Code 2017 Day 2
# Corruption Checksum
# https://adventofcode.com/2017/day/2

import sys


def parse(input: list[str]) -> list[list[int]]:
    return [sorted(map(int, line.split())) for line in input]


def part_1(input: list[str]) -> int:
    return sum(max(line) - min(line) for line in parse(input))


def part_2(input: list[str]) -> int:
    return sum(
        num2 // num1
        for line in parse(input)
        for num1 in line
        for num2 in line[line.index(num1) + 1 :]
        if num2 % num1 == 0
    )


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")

    print("Part 1:", part_1(input))  # 53460
    print("Part 2:", part_2(input))  # 282
