# Advent of Code 2024 Day 1
# Historian Hysteria
# https://adventofcode.com/2024/day/1

import sys


def parse(input: list[str]) -> tuple[list[int], list[int]]:
    lines = [map(int, line.split()) for line in input]
    lists = list(map(sorted, zip(*lines)))
    assert len(lists) == 2, "There are not two lists"
    return lists[0], lists[1]


def part_1(input: list[str]):
    left, right = parse(input)
    return sum(abs(lnum - rnum) for lnum, rnum in zip(left, right))


def part_2(input: list[str]):
    left, right = parse(input)
    return sum(lnum * right.count(lnum) for lnum in left)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")

    print("Part 1:", part_1(input))  # 3714264
    print("Part 2:", part_2(input))  # 18805872
