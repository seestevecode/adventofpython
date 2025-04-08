# Advent of Code 2015 Day 2
# I Was Told There Would Be No Math
# https://adventofcode.com/2015/day/2

import sys

if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()
    parsed = [sorted(map(int, line.split("x"))) for line in input]

    part_1: int = sum(2 * (a * b + b * c + c * a) + a * b for a, b, c in parsed)
    part_2: int = sum(2 * (a + b) + a * b * c for a, b, c in parsed)

    print("Part 1:", part_1)  # 1586300
    print("Part 2:", part_2)  # 3737498
