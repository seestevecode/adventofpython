# Advent of Code 2022 Day 1
# Calorie Counting
# https://adventofcode.com/2022/day/1

import sys

if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split("\n\n")
    parsed = [[int(item) for item in calorie_list.split()] for calorie_list in input]
    list_sums = sorted([sum(calorie_list) for calorie_list in parsed], reverse=True)

    part_1 = list_sums[0]
    part_2 = sum(list_sums[0:3])

    print("Part 1:", part_1)  # 70509
    print("Part 2:", part_2)  # 208567
