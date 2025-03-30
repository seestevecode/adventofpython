# Advent of Code 2023 Day 2
# Cube Conundrum
# https://adventofcode.com/2023/day/2

import math
import re
import sys

LIMITS = {"red": 12, "green": 13, "blue": 14}


def parse_game(game: str) -> tuple[int, dict[str, list[int]]]:
    id_str, cubes_str = game.split(": ")
    pairs = re.findall(r"(\d+) (\w+)", cubes_str)
    cube_pairs = {
        color: [int(num) for num, col in pairs if col == color] for color in LIMITS
    }
    return int(id_str.split()[1]), cube_pairs


def valid_game(counts: dict[str, list[int]]) -> int:
    return all(max(counts.get(color, [0])) <= LIMITS[color] for color in LIMITS)


def game_power(counts: dict[str, list[int]]) -> int:
    return math.prod(max(counts.get(color, [1])) for color in LIMITS)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")
    games = [parse_game(game) for game in input]

    part_1: int = sum(id for id, counts in games if valid_game(counts))
    part_2: int = sum(game_power(counts) for _, counts in games)

    print("Part 1:", part_1)  # 2617
    print("Part 2:", part_2)  # 59795
