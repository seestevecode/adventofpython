# Advent of Code 2017 Day 2
# Corruption Checksum
# https://adventofcode.com/2017/day/2

import sys

if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")
    parsed = [sorted(map(int, line.split())) for line in input]

    part_1: int = sum(max(line) - min(line) for line in parsed)
    part_2: int = sum(
        num2 // num1
        for line in parsed
        for num1 in line
        for num2 in line[line.index(num1) + 1 :]
        if num2 % num1 == 0
    )

    print("Part 1:", part_1)  # 53460
    print("Part 2:", part_2)  # 282
