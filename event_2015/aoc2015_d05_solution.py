# Advent of Code 2015 Day 5
# Doesn't He Have Intern-Elves For This?
# https://adventofcode.com/2015/day/5

import re
import sys

THREE_VOWELS = lambda x: len(re.findall(r"[aeiou]", x)) >= 3
ADJACENT = lambda x: re.search(r"(.)\1", x) is not None
NO_BAD_PAIR = lambda x: re.search(r"ab|cd|pq|xy", x) is None
TWO_PAIR = lambda x: re.search(r"(..).*\1", x) is not None
SANDWICH = lambda x: re.search(r"(.).\1", x) is not None

PART_ONE = lambda x: THREE_VOWELS(x) and ADJACENT(x) and NO_BAD_PAIR(x)
PART_TWO = lambda x: TWO_PAIR(x) and SANDWICH(x)


def part_1(input: list[str]) -> int:
    return sum(PART_ONE(line) for line in input)


def part_2(input: list[str]) -> int:
    return sum(PART_TWO(line) for line in input)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    print("Part 1:", part_1(input))  # 255
    print("Part 2:", part_2(input))  # 55
