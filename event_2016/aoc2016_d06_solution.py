# Advent of Code 2016 Day 6
# Signals and Noise
# https://adventofcode.com/2016/day/6

import sys

if __name__ == "__main__":
    input: list[str] = sys.stdin.read().strip().split()

    transposed = list(map(list, zip(*input)))
    sorted_counts = [
        sorted({char: line.count(char) for char in line}.items(), key=lambda x: x[1])
        for line in transposed
    ]
    
    part_1 = "".join([line[-1][0] for line in sorted_counts])
    part_2 = "".join([line[0][0] for line in sorted_counts])

    print("Part 1:", part_1)  # ursvoerv
    print("Part 2:", part_2)  # vomaypnn
