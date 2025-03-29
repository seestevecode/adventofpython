# Advent of Code 2018 Day 1
# Chronal Calibration
# https://adventofcode.com/2018/day/1

import itertools
import sys


def calibrate(input: list[int]):
    frequency, previous_freqs = 0, set([0])
    for change in itertools.cycle(input):
        frequency += change
        if frequency in previous_freqs:
            return frequency
        else:
            previous_freqs.add(frequency)
    raise ValueError("Previous frequency not found")


if __name__ == "__main__":
    input: str = sys.stdin.read()
    parsed = [int(line) for line in input.split()]

    part_1: int = sum(parsed)
    part_2: int = calibrate(parsed)

    print("Part 1:", part_1)  # 508
    print("Part 2:", part_2)  # 549
