# Advent of Code 2022 Day 2
# Rock Paper Scissors
# https://adventofcode.com/2022/day/2

import sys

OUTCOMES = {"win": ("AY", "BZ", "CX"), "draw": ("AX", "BY", "CZ")}
CHOICES = {"rock": ("AY", "BX", "CZ"), "paper": ("AZ", "BY", "CX")}


def parse(input: str) -> list[str]:
    return [line.replace(" ", "") for line in input.split("\n")]


def score(game: str, part: int) -> int:
    assert len(game) == 2 and game[0] in "ABC" and game[1] in "XYZ", "Invalid game"
    if part == 1:
        outcome = 6 if game in OUTCOMES["win"] else 3 if game in OUTCOMES["draw"] else 0
        choice = 1 if game[1] == "X" else 2 if game[1] == "Y" else 3
    else:
        assert part == 2, "Invalid part"
        outcome = 6 if game[1] == "Z" else 3 if game[1] == "Y" else 0
        choice = 1 if game in CHOICES["rock"] else 2 if game in CHOICES["paper"] else 3
    return outcome + choice


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    part_1 = sum(score(game, part=1) for game in parse(input))
    part_2 = sum(score(game, part=2) for game in parse(input))

    print("Part 1:", part_1)  # 11603
    print("Part 2:", part_2)  # 12725
