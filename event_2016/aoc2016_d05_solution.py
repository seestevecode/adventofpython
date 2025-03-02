# Advent of Code 2016 Day 5
# How About a Nice Game of Chess?
# https://adventofcode.com/2016/day/5

import hashlib
import sys


def solve(input: str) -> tuple[str, str]:
    counter, password1, password2 = 0, "", ["_"] * 8
    while len(password1) < 8 or "_" in password2:
        hash_input = f"{input}{counter}".encode("utf-8")
        hash_output = hashlib.md5(hash_input).hexdigest()
        if hash_output.startswith("00000"):
            if len(password1) < 8:
                password1 += hash_output[5]
            if "_" in password2:
                position = int(hash_output[5], 16)
                if position < 8 and password2[position] == "_":
                    password2[position] = hash_output[6]
        counter += 1
    return password1, "".join(password2)


if __name__ == "__main__":
    input: str = sys.stdin.read().strip()

    part_1, part_2 = solve(input)

    print("Part 1:", part_1)  # d4cd2ee1
    print("Part 2:", part_2)  # f2c7e0e5
