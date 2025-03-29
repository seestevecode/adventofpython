# Advent of Code 2022 Day 1
# Calorie Counting
# https://adventofcode.com/2022/day/1

import sys


def list_sums(input: list[list[int]]) -> list[int]:
    return sorted([sum(calorie_list) for calorie_list in input], reverse=True)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split("\n\n")
    parsed = [[int(item) for item in calorie_list.split()] for calorie_list in input]

    part_1 = list_sums(parsed)[0]
    part_2 = sum(list_sums(parsed)[0:3])

    print("Part 1:", part_1)  # 70509
    print("Part 2:", part_2)  # 208567
