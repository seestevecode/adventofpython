# Advent of Code 2022 Day 1
# Calorie Counting
# https://adventofcode.com/2022/day/1

import sys


def list_sums(input: list[str]) -> list[int]:
    parsed = [[int(item) for item in calorie_list.split()] for calorie_list in input]
    return sorted([sum(calorie_list) for calorie_list in parsed], reverse=True)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split("\n\n")

    part_1 = list_sums(input)[0]
    part_2 = sum(list_sums(input)[0:3])

    print("Part 1:", part_1)  # 70509
    print("Part 2:", part_2)  # 208567
