# Advent of Code 2020 Day 6
# Custom Customs
# https://adventofcode.com/2020/day/6

import sys


def common_answers(group: str) -> set[str]:
    answer_sets = [set(answers) for answers in group.split()]
    return answer_sets[0].intersection(*answer_sets)


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().split("\n\n")

    part_1: int = sum(len(set(group.replace("\n", ""))) for group in input)
    part_2: int = sum(len(common_answers(group)) for group in input)

    print("Part 1:", part_1)  # 6630
    print("Part 2:", part_2)  # 3437
