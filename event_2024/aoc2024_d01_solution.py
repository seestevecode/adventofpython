# Advent of Code 2024 Day 1
# Historian Hysteria
# https://adventofcode.com/2024/day/1

import sys


def parse(input: list[str]) -> tuple[list[int], list[int]]:
    lines = [map(int, line.split()) for line in input]
    lists = list(map(sorted, zip(*lines)))
    assert len(lists) == 2, "There are not two lists"
    return lists[0], lists[1]


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")

    left, right = parse(input)

    part_1 = sum(abs(lnum - rnum) for lnum, rnum in zip(left, right))
    part_2 = sum(lnum * right.count(lnum) for lnum in left)

    print("Part 1:", part_1)  # 3714264
    print("Part 2:", part_2)  # 18805872
