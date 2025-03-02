# Advent of Code 2016 Day 2
# Bathroom Security
# https://adventofcode.com/2016/day/2

import sys

DELTAS = {"U": (0, -1), "R": (1, 0), "D": (0, 1), "L": (-1, 0)}

GRID_1 = "123\n456\n789"
GRID_2 = "..1..\n.234.\n56789\n.ABC.\n..D.."


def solve(input: list[str], grid: str) -> str:
    sgrid = grid.split()
    assert len({len(row) for row in sgrid}) == 1, "Malformed grid"
    rows, cols = len(sgrid), len(sgrid[0])
    grid_x, grid_y = -1, -1
    for rownum, row in enumerate(sgrid):
        if "5" in row:
            grid_x, grid_y = row.index("5"), rownum
    result = ""
    for line in input:
        for move in line:
            new_x = grid_x + DELTAS[move][0]
            new_y = grid_y + DELTAS[move][1]
            if new_x not in range(cols) or new_y not in range(rows):
                continue
            if sgrid[new_y][new_x] != ".":
                grid_x, grid_y = new_x, new_y
        result += sgrid[grid_y][grid_x]
    return result


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split()

    part_1 = solve(input, GRID_1)
    part_2 = solve(input, GRID_2)

    print("Part 1:", part_1)  # 52981
    print("Part 2:", part_2)  # 74CD2
