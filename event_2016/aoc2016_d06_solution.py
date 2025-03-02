# Advent of Code 2016 Day 6
# Signals and Noise
# https://adventofcode.com/2016/day/6

import sys


def solve(input: list[str]) -> tuple[str, str]:
    transposed = list(map(list, zip(*input)))
    sorted_counts = [
        sorted({char: line.count(char) for char in line}.items(), key=lambda x: x[1])
        for line in transposed
    ]
    most_common = "".join([line[-1][0] for line in sorted_counts])
    least_common = "".join([line[0][0] for line in sorted_counts])
    return most_common, least_common


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split()

    part_1, part_2 = solve(input)

    print("Part 1:", part_1)  # ursvoerv
    print("Part 2:", part_2)  # vomaypnn
