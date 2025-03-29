# Advent of Code 2023 Day 1
# Trebuchet?!
# https://adventofcode.com/2023/day/1

import sys

NUMBERS = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")


def replace_1(string: str) -> str:
    return "".join(char for char in string if char in "123456789")


def replace_2(string: str) -> str:
    return "".join(
        [
            str(NUMBERS.index(word) + 1) if string[i:].startswith(word) else string[i]
            for i in range(len(string))
            for word in NUMBERS
            if string[i].isdigit() or string[i:].startswith(word)
        ]
    )


def to_num(string: str, replace_func) -> int:
    replaced = replace_func(string)
    return int(replaced[0] + replaced[-1])


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    part_1: int = sum(to_num(line, replace_1) for line in input)
    part_2: int = sum(to_num(line, replace_2) for line in input)

    print("Part 1:", part_1)  # 53334
    print("Part 2:", part_2)  # 52834
