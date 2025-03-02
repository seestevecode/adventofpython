# Advent of Code 2015 Day 1
# Not Quite Lisp
# https://adventofcode.com/2015/day/1

import sys


def part_1(input: str) -> int:
    return input.count("(") - input.count(")")


def part_2(input: str) -> int | None:
    floor = 0
    return next(
        (
            step
            for step, move in enumerate(input, start=1)
            if (floor := floor + (1 if move == "(" else -1 if move == ")" else 0)) == -1
        ),
        None,
    )


if __name__ == "__main__":
    input: str = sys.stdin.read()

    print("Part 1:", part_1(input))  # 280
    print("Part 2:", part_2(input))  # 1797
