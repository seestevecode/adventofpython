# Advent of Code 2016 Day 4
# Security Through Obscurity
# https://adventofcode.com/2016/day/4

import re
import sys
from string import ascii_lowercase as letters


def parse(room: str) -> tuple[str, int, str]:
    pattern = r"^([a-z-]+)-(\d+)\[([a-z]+)\]$"
    match = re.match(pattern, room)
    if match:
        return match.group(1), int(match.group(2)), match.group(3)
    raise ValueError("Invalid room")


def part_1(input: list[str]) -> int:
    def decrypt_name(name: str) -> str:
        counts = {char: name.count(char) for char in name.replace("-", "")}
        sorted_counts = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
        return "".join(map(lambda x: x[0], sorted_counts))[:5]

    return sum(
        sector_id
        for room in input
        if (
            name := parse(room)[0],
            sector_id := parse(room)[1],
            checksum := parse(room)[2],
        )
        and decrypt_name(name) == checksum
    )


def part_2(input: list[str]) -> int:
    def decipher_room(room: str) -> tuple[str, int]:
        def rotate(char: str, offset: int) -> str:
            return letters[(letters.index(char) + offset) % 26]

        name, sector_id, _ = parse(room)
        return (
            "".join([rotate(char, sector_id) if char != "-" else " " for char in name]),
            sector_id,
        )

    return next(
        decipher_room(room)[1]
        for room in input
        if "object storage" in decipher_room(room)[0]
    )


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    print("Part 1:", part_1(input))  # 361724
    print("Part 2:", part_2(input))  # 482
