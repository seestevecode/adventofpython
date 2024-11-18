from pathlib import Path

MOVES = {"^": (0, 1), ">": (1, 0), "v": (0, -1), "<": (-1, 0)}


def move(start, direction):
    start_x, start_y = start
    return (start_x + MOVES[direction][0], start_y + MOVES[direction][1])


def part_one(input):
    location, visited = (0, 0), {(0, 0)}
    for direction in input:
        location = move(location, direction)
        visited.add(location)
    return len(visited)


def part_two(input):
    location_santa, visited_santa = (0, 0), {(0, 0)}
    location_robot, visited_robot = (0, 0), {(0, 0)}
    for direction_santa, direction_robot in [
        (input[idx], input[idx + 1]) for idx in range(0, len(input) - 1, 2)
    ]:
        location_santa = move(location_santa, direction_santa)
        location_robot = move(location_robot, direction_robot)
        visited_santa.add(location_santa)
        visited_robot.add(location_robot)
    return len(visited_santa | visited_robot)


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read().strip()

    print("Part one:", part_one(input))
    print("Part two:", part_two(input))
