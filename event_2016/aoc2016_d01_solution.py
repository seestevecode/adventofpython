# Advent of Code 2016 Day 1
# No Time for a Taxicab
# https://adventofcode.com/2016/day/1

import sys

DELTAS = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}


def parse(input: str) -> list[tuple[str, int]]:
    return [(instr[0], int(instr[1:])) for instr in input.split(", ")]


def new_facing(old_facing: int, turn_direction: str) -> int:
    assert old_facing in [0, 90, 180, 270], "Invalid facing direction"
    assert turn_direction in "RL", "Invalid turn direction"
    return (old_facing + (90 if turn_direction == "R" else -90)) % 360


def new_location(
    old_location: tuple[int, int], facing: int, distance: int
) -> tuple[int, int]:
    coord_x, coord_y = old_location
    coord_x += DELTAS[facing][0] * distance
    coord_y += DELTAS[facing][1] * distance
    return (coord_x, coord_y)


def manhatten(loc: tuple[int, int]) -> int:
    return abs(loc[0]) + abs(loc[1])


def solve(input: str) -> tuple[int, int]:
    location, facing, visited_locs = (0, 0), 0, set([(0, 0)])
    part_1, part_2 = 0, 0
    for turn_dir, distance in parse(input):
        facing = new_facing(facing, turn_dir)
        for _ in range(distance):
            location = new_location(location, facing, 1)
            if location in visited_locs and not part_2:
                part_2 = manhatten(location)
            else:
                visited_locs.add(location)
    part_1 = manhatten(location)
    return part_1, part_2


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    print("Part 1:", solve(input)[0])  # 353
    print("Part 2:", solve(input)[1])  # 152
