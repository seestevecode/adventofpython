# Advent of Code 2018 Day 1
# Chronal Calibration
# https://adventofcode.com/2018/day/1

import itertools
import sys


def parse(input: str) -> list[int]:
    return [int(line) for line in input.split()]


def part_1(input: str) -> int:
    return sum(parse(input))


def part_2(input: str) -> int:
    frequency, previous_freqs = 0, set([0])
    for change in itertools.cycle(parse(input)):
        frequency += change
        if frequency in previous_freqs:
            return frequency
        else:
            previous_freqs.add(frequency)
    return -1


if __name__ == "__main__":
    input: str = sys.stdin.read()

    print("Part 1:", part_1(input))  # 508
    print("Part 2:", part_2(input))  # 549
