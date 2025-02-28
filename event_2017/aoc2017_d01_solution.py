# Advent of Code 2017 Day 1
# Inverse Captcha
# https://adventofcode.com/2017/day/1

import sys


def solve(input: str, offset: int = 1) -> int:
    parsed = [int(char) for char in input]
    offset_parsed = parsed[offset:] + parsed[:offset]
    return sum(num1 for num1, num2 in zip(parsed, offset_parsed) if num1 == num2)


def part_1(input: str) -> int:
    return solve(input)


def part_2(input: str) -> int:
    return solve(input, offset=len(input) // 2)


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    print("Part 1:", part_1(input))  # 1390
    print("Part 2:", part_2(input))  # 1232
