# Advent of Code 2020 Day 3
# Toboggan Trajectory
# https://adventofcode.com/2020/day/3

import sys
from math import prod

TRAJECTORIES = [(1, 3), (1, 1), (1, 5), (1, 7), (2, 1)]


def tree_count(input: str, step_down: int, step_right: int) -> int:
    row_pos, col_pos, trees_hit = 0, 0, 0
    grid = [[char for char in row] for row in input.split()]
    assert len({len(row) for row in grid}) == 1, "Malformed grid"
    grid_rows, grid_cols = len(grid), len(grid[0])
    while row_pos < grid_rows:
        trees_hit += grid[row_pos][col_pos] == "#"
        row_pos += step_down
        col_pos = (col_pos + step_right) % grid_cols
    return trees_hit


if __name__ == "__main__":
    input: str = sys.stdin.read()

    part_1 = tree_count(input, *TRAJECTORIES[0])
    part_2 = prod(tree_count(input, *trajectory) for trajectory in TRAJECTORIES)

    print("Part 1:", part_1)  # 207
    print("Part 2:", part_2)  # 2655892800
