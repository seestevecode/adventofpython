# Advent of Code 2020 Day 4
# Passport Processing
# https://adventofcode.com/2020/day/4

import sys

KEY_FUNCS = {
    "byr": lambda x: len(x) == 4 and x.isdigit() and 1920 <= int(x) <= 2002,
    "iyr": lambda x: len(x) == 4 and x.isdigit() and 2010 <= int(x) <= 2020,
    "eyr": lambda x: len(x) == 4 and x.isdigit() and 2020 <= int(x) <= 2030,
    "hgt": lambda x: valid_height(x),
    "hcl": lambda x: valid_hair_colour(x),
    "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda x: len(x) == 9 and x.isdigit(),
}


def valid_height(height: str):
    value, unit = height[:-2], height[-2:]
    if value.isdigit() and unit in ("cm", "in"):
        return 150 <= int(value) <= 193 if unit == "cm" else 59 <= int(value) <= 76
    return False


def valid_hair_colour(hair_colour: str):
    return (
        len(hair_colour) == 7
        and hair_colour.startswith("#")
        and set(hair_colour[1:]).issubset(set("0123456789abcdef"))
    )


def check_keys(passport: str) -> bool:
    return all(key in passport for key in KEY_FUNCS.keys())


def check_vals(passport: str) -> bool:
    pairs = {pair.split(":")[0]: pair.split(":")[1] for pair in passport.split()}
    return all(KEY_FUNCS[key](value) for key, value in pairs.items() if key != "cid")


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split("\n\n")

    part_1: int = sum(check_keys(passport) for passport in input)
    part_2: int = sum(
        check_keys(passport) and check_vals(passport) for passport in input
    )

    print("Part 1:", part_1)  # 216
    print("Part 2:", part_2)  # 150
