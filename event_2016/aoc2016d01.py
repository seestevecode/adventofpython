from pathlib import Path


def parse(input):
    return [(inst[0], int(inst[1:])) for inst in input.strip().split(", ")]


def turn(turn_dir, facing):
    return "NESW"[("NESW".index(facing) + (1 if turn_dir == "R" else -1)) % 4]


def move(facing, distance, coord_x, coord_y):
    coord_x += distance if facing == "E" else -distance if facing == "W" else 0
    coord_y += distance if facing == "N" else -distance if facing == "S" else 0
    return coord_x, coord_y


def part_one(input):
    facing, coord_x, coord_y = "N", 0, 0
    for turn_dir, distance in parse(input):
        facing = turn(turn_dir, facing)
        coord_x, coord_y = move(facing, distance, coord_x, coord_y)
    return abs(coord_x) + abs(coord_y)


def part_two(input):
    facing, coord_x, coord_y = "N", 0, 0
    visited = [(0, 0)]
    for turn_dir, distance in parse(input):
        facing = turn(turn_dir, facing)
        for _ in range(distance):
            coord_x, coord_y = move(facing, 1, coord_x, coord_y)
            if (coord_x, coord_y) in visited:
                return abs(coord_x) + abs(coord_y)
            else:
                visited.append((coord_x, coord_y))
    return None  # shouldn't ever reach here


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read()

    print("Part one:", part_one(input))
    print("Part two:", part_two(input))
