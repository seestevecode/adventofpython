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

if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    part_1: int = sum(
        THREE_VOWELS(line) and ADJACENT(line) and NO_BAD_PAIR(line) for line in input
    )
    part_2: int = sum(TWO_PAIR(line) and SANDWICH(line) for line in input)

    print("Part 1:", part_1)  # 255
    print("Part 2:", part_2)  # 55
