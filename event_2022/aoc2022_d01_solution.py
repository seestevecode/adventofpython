# Advent of Code 2022 Day 1
# Calorie Counting
# https://adventofcode.com/2022/day/1

import sys


def list_sums(input: list[str]) -> list[int]:
    parsed = [[int(item) for item in calorie_list.split()] for calorie_list in input]
    return sorted([sum(calorie_list) for calorie_list in parsed], reverse=True)


def part_1(input: list[str]):
    return list_sums(input)[0]


def part_2(input: list[str]):
    return sum(list_sums(input)[0:3])


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split("\n\n")

    print("Part 1:", part_1(input))  # 70509
    print("Part 2:", part_2(input))  # 208567
