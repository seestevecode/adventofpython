# Advent of Code 2016 Day 3
# Square With Three Sides
# https://adventofcode.com/2016/day/3

import sys


def valid(triangle: list[int]) -> bool:
    assert len(triangle) == 3, "There aren't three sides"
    a, b, c = triangle
    return a + b > c and b + c > a and c + a > b


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    parsed = [list(map(int, line.split())) for line in input.split("\n")]
    transposed = [
        [parsed[i][col], parsed[i + 1][col], parsed[i + 2][col]]
        for i in range(0, len(parsed), 3)
        for col in range(3)
    ]

    part_1: int = sum(valid(triangle) for triangle in parsed)
    part_2: int = sum(valid(triangle) for triangle in transposed)

    print("Part 1:", part_1)  # 917
    print("Part 2:", part_2)  # 1649
