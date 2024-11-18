from pathlib import Path


def parse(input):
    return [sorted(map(int, line.split("x"))) for line in input.split()]


def part_one(input):
    return sum(2 * (a * b + b * c + c * a) + a * b for a, b, c in parse(input))


def part_two(input):
    return sum(2 * (a + b) + a * b * c for a, b, c in parse(input))


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read()

    print("Part one:", part_one(input))
    print("Part two:", part_two(input))
