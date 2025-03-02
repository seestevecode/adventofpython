# Advent of Code 2015 Day 3
# Perfectly Spherical Houses in a Vacuum
# https://adventofcode.com/2015/day/3

import sys

MOVES = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def visited(input: str) -> set[tuple[int, int]]:
    coord_x, coord_y, visited = 0, 0, {(0, 0)}
    for move in input:
        coord_x += MOVES[move][0]
        coord_y += MOVES[move][1]
        visited.add((coord_x, coord_y))
    return visited


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    part_1 = len(visited(input))
    part_2 = len(visited(input[0::2]) | visited(input[1::2]))

    print("Part 1:", part_1)  # 2081
    print("Part 2:", part_2)  # 2341
