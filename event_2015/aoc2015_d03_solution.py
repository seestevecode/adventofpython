# Advent of Code 2015 Day 3
# Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3

import sys
from itertools import accumulate

MOVES = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def visited(input: str) -> set[tuple[int, int]]:
    steps = (MOVES[move] for move in input)
    positions = accumulate(steps, lambda x, y: (x[0] + y[0], x[1] + y[1]))
    return {(0, 0), *positions}


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    part_1: int = len(visited(input))
    part_2: int = len(visited(input[0::2]) | visited(input[1::2]))

    print("Part 1:", part_1)  # 2081
    print("Part 2:", part_2)  # 2341
