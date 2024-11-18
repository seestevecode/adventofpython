import re
from pathlib import Path

NICE_PART_ONE = (
    lambda string: len(re.findall(r"[aeiou]", string)) >= 3
    and re.search(r"(.)\1", string) is not None
    and re.search(r"ab|cd|pq|xy", string) is None
)

NICE_PART_TWO = (
    lambda string: re.search(r"(..).*\1", string) is not None
    and re.search(r"(.).\1", string) is not None
)


def solve(input, nice_func):
    return len([string for string in input if nice_func(string)])


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read().split()

    part_one = solve(input, NICE_PART_ONE)
    part_two = solve(input, NICE_PART_TWO)

    print("Part one:", part_one)
    print("Part two:", part_two)
