# Advent of Code 2020 Day 5
# Binary Boarding
# https://adventofcode.com/2020/day/5

import sys


def seat_id(seat_str: str) -> int:
    assert len(seat_str) == 10, "Seat string incorrect length"
    row = int(seat_str[:7].replace("F", "0").replace("B", "1"), 2)
    seat = int(seat_str[7:].replace("L", "0").replace("R", "1"), 2)
    return row * 8 + seat


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    part_1: int = max(seat_id(seat) for seat in input)

    id_set = {seat_id(seat) for seat in input}
    missing_id = set(range(min(id_set), max(id_set) + 1)) - id_set
    assert len(missing_id) == 1, "There isn't a unique missing Id"
    part_2: int = missing_id.pop()

    print("Part 1:", part_1)  # 816
    print("Part 2:", part_2)  # 539
