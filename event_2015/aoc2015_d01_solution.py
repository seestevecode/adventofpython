# Advent of Code 2015 Day 1
# Not Quite Lisp
# https://adventofcode.com/2015/day/1

import sys
from itertools import accumulate


def basement_step(input: str) -> int:
    moves = (1 if c == "(" else -1 for c in input)
    floors = accumulate(moves)
    for step, floor in enumerate(floors, start=1):
        if floor == -1:
            return step
    raise ValueError("Floor -1 not reached")


if __name__ == "__main__":
    input: str = sys.stdin.read()

    part_1: int = input.count("(") - input.count(")")
    part_2: int = basement_step(input)

    print("Part 1:", part_1)  # 280
    print("Part 2:", part_2)  # 1797
