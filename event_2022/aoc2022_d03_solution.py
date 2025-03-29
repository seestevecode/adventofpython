# Advent of Code 2022 Day 3
# Rucksack Reorganization
# https://adventofcode.com/2022/day/3

import sys
from string import ascii_lowercase, ascii_uppercase


def priority(*strings):
    intersect = set.intersection(*[set(string) for string in strings])
    assert len(intersect) == 1, "There is more than one common character"
    return (ascii_lowercase + ascii_uppercase).index(intersect.pop()) + 1


def split_rucksack(rucksack: str) -> tuple[str, str]:
    assert len(rucksack) % 2 == 0, "Rucksack has odd number of items"
    midpoint = len(rucksack) // 2
    return rucksack[:midpoint], rucksack[midpoint:]


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    part_1: int = sum(priority(*split_rucksack(rucksack)) for rucksack in input)

    assert len(input) % 3 == 0, "Number of elves is not a multiple of 3"
    chunked = [input[i : i + 3] for i in range(0, len(input), 3)]
    part_2: int = sum(priority(*group) for group in chunked)

    print("Part 1:", part_1)  # 8252
    print("Part 2:", part_2)  # 2828
