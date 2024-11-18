from pathlib import Path

ACTIONS_PART_ONE = {
    "on": lambda _: 1,
    "off": lambda _: 0,
    "toggle": lambda x: 1 if x == 0 else 0,
}
ACTIONS_PART_TWO = {
    "on": lambda x: x + 1,
    "off": lambda x: max(0, x - 1),
    "toggle": lambda x: x + 2,
}


def get_coord_range(coord_1, coord_2):
    x1, y1 = coord_1
    x2, y2 = coord_2
    min_x, max_x, min_y, max_y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
    return [(x, y) for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1)]


def solve(input, actions):
    grid = {(x, y): 0 for x in range(1000) for y in range(1000)}
    for line in input:
        if line.startswith("turn"):
            _, action, coord_1, _, coord_2 = line.split()
        else:
            assert line.startswith("toggle")
            action, coord_1, _, coord_2 = line.split()
        coord_1 = map(int, coord_1.split(","))
        coord_2 = map(int, coord_2.split(","))
        for x, y in get_coord_range(coord_1, coord_2):
            grid[(x, y)] = (actions[action])(grid[(x, y)])
    return sum(grid.values())


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.readlines()

    part_one = solve(input, ACTIONS_PART_ONE)
    part_two = solve(input, ACTIONS_PART_TWO)

    print("Part one:", part_one)
    print("Part two:", part_two)
