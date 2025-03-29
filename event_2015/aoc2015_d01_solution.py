# Advent of Code 2015 Day 1
# Not Quite Lisp
# https://adventofcode.com/2015/day/1

import sys


def basement_step(input: str) -> int:
    floor = 0
    for step, move in enumerate(input, start=1):
        floor += 1 if move == "(" else -1 if move == ")" else 0
        if floor == -1:
            return step
    raise ValueError("Floor -1 not reached")


if __name__ == "__main__":
    input: str = sys.stdin.read()

    part_1: int = input.count("(") - input.count(")")
    part_2: int = basement_step(input)

    print("Part 1:", part_1)  # 280
    print("Part 2:", part_2)  # 1797
