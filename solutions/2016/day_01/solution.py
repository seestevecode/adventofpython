# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2016/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2016
    _day = 1
    separator = ", "

    @answer((353, 152))
    def solve(self) -> tuple[int, int]:
        coord_x, coord_y, facing, visited, first_repeat = 0, 0, 0, [(0, 0)], 0

        for turn, distance in [(step[0], int(step[1:])) for step in self.input]:
            facing = (facing + (90 if turn == "R" else -90 if turn == "L" else 0)) % 360

            for _ in range(distance):
                coord_x += 1 if facing == 90 else -1 if facing == 270 else 0
                coord_y += 1 if facing == 0 else -1 if facing == 180 else 0

                if (coord_x, coord_y) in visited and not first_repeat:
                    first_repeat = abs(coord_x) + abs(coord_y)

                visited.append((coord_x, coord_y))

        return abs(coord_x) + abs(coord_y), first_repeat
