# Advent of Code 2024 Day 2
# Red-Nosed Reports
# https://adventofcode.com/2024/day/2

import sys


def safe_report(report: list[int]) -> bool:
    sequential = report in [sorted(report), sorted(report, reverse=True)]
    gaps_1to3 = all(1 <= abs(x - y) <= 3 for x, y in zip(report, report[1:]))
    return sequential and gaps_1to3


def safe_dampened(report: list[int]) -> bool:
    return any(safe_report(report[:i] + report[i + 1 :]) for i in range(len(report)))


if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split("\n")
    parsed = [list(map(int, report.split())) for report in input]

    part_1: int = sum(safe_report(report) for report in parsed)
    part_2: int = sum(safe_report(report) or safe_dampened(report) for report in parsed)

    print("Part 1:", part_1)  # 585
    print("Part 2:", part_2)  # 626
