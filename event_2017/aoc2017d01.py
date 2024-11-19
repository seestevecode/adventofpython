from pathlib import Path


def solve(input, offset):
    return sum(
        int(n1) for n1, n2 in zip(input, input[offset:] + input[:offset]) if n1 == n2
    )


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read().strip()

    part_one = solve(input, 1)
    part_two = solve(input, len(input) // 2)

    print("Part one:", part_one)
    print("Part two:", part_two)
