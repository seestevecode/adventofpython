from pathlib import Path

KEYPAD_ONE = """\
123
456
789"""

KEYPAD_TWO = """\
..1..
.234.
56789
.ABC.
..D.."""


def find_in_nested(outer, target):
    for inner in outer:
        if target in inner:
            return outer.index(inner), inner.index(target)
    raise ValueError("Not found in nested list")


def solve(keypad, input):
    key_from, code = "5", []
    keypad = keypad.split()
    if len({len(row) for row in keypad}) != 1:
        raise ValueError("Invalid keypad", keypad)
    blanks = "." * (len(keypad[0]) + 2)
    padded_keypad = [blanks] + [f".{line}." for line in keypad] + [blanks]
    for line in input:
        for dir in line:
            row, col = find_in_nested(padded_keypad, key_from)
            row += 1 if dir == "D" else -1 if dir == "U" else 0
            col += 1 if dir == "R" else -1 if dir == "L" else 0
            key_to = padded_keypad[row][col]
            key_from = key_from if key_to == "." else key_to
        code.append(key_from)
    return "".join(map(str, code))


if __name__ == "__main__":
    aoc_dir = Path(__file__).parents[2]
    event_dir_name = Path(__file__).parent.stem
    file_name = Path(__file__).stem
    with open(aoc_dir / "inputs" / event_dir_name / file_name) as f:
        input = f.read().split()

    part_one = solve(KEYPAD_ONE, input)
    part_two = solve(KEYPAD_TWO, input)

    print("Part one:", part_one)
    print("Part two:", part_two)
