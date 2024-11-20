import itertools
from pathlib import Path

# TEST_INPUT has an extra line break for legibility, stripped later
TEST_INPUT = """\
+1
-1
"""


def read(input):
    """Read input from inputs/ folder"""
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read()
    return input


def parse(input):
    """Parse input to a list of integers"""
    return [int(num) for num in input.split()]


def part_one(input):
    """Part one: Sum the integers"""
    return sum(parse(input))


def part_two(input):
    """Find the first frequency reached twice"""
    found_frequencies = {0}
    for frequency in itertools.accumulate(itertools.cycle(parse(input))):
        if frequency in found_frequencies:
            return frequency
        found_frequencies.add(frequency)


if __name__ == "__main__":
    # input = TEST_INPUT.strip()
    input = read(input)

    print("Part one:", part_one(input))
    print("Part two:", part_two(input))
