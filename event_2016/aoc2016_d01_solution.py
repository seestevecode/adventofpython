# Advent of Code 2016 Day 1
# No Time for a Taxicab
# https://adventofcode.com/2016/day/1

import sys

DELTAS = {0: (0, -1), 90: (1, 0), 180: (0, 1), 270: (-1, 0)}


def manhatten(loc: tuple[int, int]) -> int:
    return abs(loc[0]) + abs(loc[1])


def solve(input: str) -> tuple[int, int]:
    coord, facing, visited_coords = (0, 0), 0, set([(0, 0)])
    part_1, part_2 = 0, 0
    parsed = [(instr[0], int(instr[1:])) for instr in input.split(", ")]
    for turn_dir, distance in parsed:
        assert facing in [0, 90, 180, 270], "Invalid facing direction"
        assert turn_dir in "RL", "Invalid turn direction"
        facing = (facing + (90 if turn_dir == "R" else -90)) % 360
        for _ in range(distance):
            coord = (coord[0] + DELTAS[facing][0], coord[1] + DELTAS[facing][1])
            if coord in visited_coords and not part_2:
                part_2 = manhatten(coord)
            else:
                visited_coords.add(coord)
    part_1 = manhatten(coord)
    return part_1, part_2


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    part_1, part_2 = solve(input)

    print("Part 1:", part_1)  # 353
    print("Part 2:", part_2)  # 152
