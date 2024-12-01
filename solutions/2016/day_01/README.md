# Day 1 (2016)

`No Time for a Taxicab` ([prompt](https://adventofcode.com/2016/day/1))

Solved this one as a single function, with a more imperative approach. I used the `StrSplitSolution` import class with `", "` as the separator. I could equally have done it using the base template and done the splitting manually.

```python
    coord_x, coord_y, facing, visited, first_repeat = 0, 0, 0, [(0, 0)], 0
```

Start by initiating our variables. `coord_x` and `coord_y` give us our current location. `facing` is the direction we're facing, expressed as a compass bearing, e.g. 0, 90, 180 or 270. `visited` is a list of coordinate tuples. `first_repeat` is the Manhatten distance for the first coordinate we reach twice, i.e. the solution to Part 2.

```python
    for turn, distance in [(step[0], int(step[1:])) for step in self.input]:
```

We iterate through the input (remember this is a list of 'instructions') and split each one using the first character with `step[0]` to get the turn direction, i.e. "R" or "L", and the rest of the string turned to an int with `int(step[1:])` to get the distance.

```python
        facing = (facing + (90 if turn == "R" else -90 if turn == "L" else 0)) % 360
```

First thing to do is to turn. We increment `facing` by 90 for a right turn, -90 for a left turn, or no change. We use `% 360` to make sure we keep the `facing` value under 360.

```python
        for _ in range(distance):
```

We want to process our steps once for each step in the distance so loop through that range. We don't need to keep the step number, so we drop that by using `_`.

```python
            coord_x += 1 if facing == 90 else -1 if facing == 270 else 0
            coord_y += 1 if facing == 0 else -1 if facing == 180 else 0
```

Increment the X (East/West) coordinate by 1 if we're facing East (90), by -1 if we're facing West (270) or no change. Similarly for `coord_y`, the North/South coordinate if we're facing North (0) or South (180) respectively.

```python
            if (coord_x, coord_y) in visited and not first_repeat:
                first_repeat = abs(coord_x) + abs(coord_y)
```

If the location (coordinate pair) we've just arrived at is not in the `visited` list AND we DON'T already have a `first_repeat` (anything non-zero is 'truthy'), we calculate the Manhatten distance for the current location and assign it to the `first_repeat` variable.

```python
            visited.append((coord_x, coord_y))
```

Now we add the current location (as a coordinate tuple) to the `visited` list. This is needed for Part 1, but not Part 2.

```python
    return abs(coord_x) + abs(coord_y), first_repeat
```

After finishing travelling the distance for every instruction, i.e. ending both loops, we return a tuple containing the Manhatten distance for the final destination and the `first_repeat`.
