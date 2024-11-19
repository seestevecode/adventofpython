from pathlib import Path


def parse(input):
    return [list(map(int, row.split())) for row in input]


def part_one(input):
    return sum(max(row) - min(row) for row in parse(input))


def part_two(input):
    divisors = []
    for row in parse(input):
        divisors.append([y // x for x in row for y in row if x != y and y % x == 0])
    return sum(divisor for sublist in divisors for divisor in sublist)


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read().strip().split("\n")

    print("Part one:", part_one(input))
    print("Part two:", part_two(input))
