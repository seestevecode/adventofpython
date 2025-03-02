# Advent of Code 2015 Day 4
# The Ideal Stocking Stuffer
# https://adventofcode.com/2015/day/4

import hashlib
import itertools
import sys


def solve(input: str, prefix: str) -> int:
    for num in itertools.count():
        hash_input = f"{input}{num}".encode()
        hash_result = hashlib.md5(hash_input).hexdigest()
        if hash_result.startswith(prefix):
            return num
    raise ValueError("No result found")


def part_1(input: str) -> int:
    return solve(input, "00000")


def part_2(input: str) -> int:
    return solve(input, "000000")


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    print("Part 1:", part_1(input))  # 117946
    print("Part 2:", part_2(input))  # 3938038
