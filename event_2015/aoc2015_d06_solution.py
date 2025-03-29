# Advent of Code 2015 Day 6
# Probably a Fire Hazard
# https://adventofcode.com/2015/day/6

import re
import sys
from itertools import product

ACTIONS_1 = {
    "turn on": lambda _: 1,
    "turn off": lambda _: 0,
    "toggle": lambda x: 1 if x == 0 else 0,
}

ACTIONS_2 = {
    "turn on": lambda x: x + 1,
    "turn off": lambda x: max(0, x - 1),
    "toggle": lambda x: x + 2,
}


def solve(input: list[str], actions: dict) -> int:

    def parse(instruction: str) -> tuple[str, int, int, int, int]:
        pattern = r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)"
        match = re.match(pattern, instruction)
        if match:
            action = match.group(1)
            x1, y1 = (int(match.group(2)), int(match.group(3)))
            x2, y2 = (int(match.group(4)), int(match.group(5)))
            return action, x1, y1, x2, y2
        raise ValueError("Invalid instruction")

    grid = {(x, y): 0 for x in range(1000) for y in range(1000)}
    for line in input:
        action, x1, y1, x2, y2 = parse(line)
        grid_updates = {
            (x, y): actions[action](grid[(x, y)])
            for x, y in product(range(x1, x2 + 1), range(y1, y2 + 1))
        }
        grid.update(grid_updates)
    return sum(grid.values())


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")

    part_1: int = solve(input, ACTIONS_1)
    part_2: int = solve(input, ACTIONS_2)

    print("Part 1:", part_1)  # 569999
    print("Part 2:", part_2)  # 17836115
