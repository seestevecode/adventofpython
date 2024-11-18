from pathlib import Path


def part_one(input):
    return input.count("(") - input.count(")")


def part_two(input):
    floor = 0
    for position, instruction in enumerate(input, start=1):
        floor += 1 if instruction == "(" else -1 if instruction == ")" else 0
        if floor == -1:
            return position
    return "No solution found"


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read()

    print("Part one:", part_one(input))
    print("Part two:", part_two(input))
