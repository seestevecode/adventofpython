import hashlib
from pathlib import Path


def solve(start_string, input):
    num = 1
    while (
        not hashlib.md5((input + str(num)).encode())
        .hexdigest()
        .startswith(start_string)
    ):
        num += 1
    return num


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read().strip()

    part_one = solve("00000", input)
    part_two = solve("000000", input)

    print("Part one:", part_one)
    print("Part two:", part_two)
