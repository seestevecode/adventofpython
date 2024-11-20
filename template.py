from pathlib import Path

TEST_INPUT = """\
test
your
input
here
"""


def read(input):
    """Read the input from the inputs/ folder"""
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read()
    return input


def part_one(input):
    pass


def part_two(input):
    pass


if __name__ == "__main__":
    input = TEST_INPUT.strip()
    # input = read(input)

    print("Part one:", part_one(input))
    print("Part two:", part_two(input))
