# Advent of Code 2024 Day 1
# Historian Hysteria
# https://adventofcode.com/2024/day/1

import sys

if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")

    lines = [map(int, line.split()) for line in input]
    lists = list(map(sorted, zip(*lines)))
    assert len(lists) == 2, "There are not two lists"
    left, right = lists[0], lists[1]

    part_1: int = sum(abs(lnum - rnum) for lnum, rnum in zip(left, right))
    part_2: int = sum(lnum * right.count(lnum) for lnum in left)

    print("Part 1:", part_1)  # 3714264
    print("Part 2:", part_2)  # 18805872
