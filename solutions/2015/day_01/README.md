# Day 1 (2015)

`Not Quite Lisp` ([prompt](https://adventofcode.com/2015/day/1))

1. Start at floor 0 having made 0 steps. Iterate through the input using `enumerate()` to keep an index (`step`) and making sure we start at step 1 rather than the default of 0.

```python
    floor, steps = 0, 0
    for step, move in enumerate(self.input, start=1):
```

2. With each iteration, increment the floor by 1 for `(`, by -1 (i.e. decrease by 1) for `)` or else remain unchanged.

```python
        floor += 1 if move == "(" else -1 if move == ")" else 0
```

3. After each iteration, check if we've reached floor -1 and we haven't already populated the `steps` variable, then assign the current `step` number to `steps`. This will solve Part 2.

```python
        if floor == -1 and not steps:
            steps = step
```

4. At the end of the iteration, return the current `floor` (Part 1) and the number of `steps` to reach floor -1 (Part 2) in a tuple.

```python
    return floor, steps
```

NB Part 1 could have been done by just counting the number of `(` and subtracting the number of `)`.
