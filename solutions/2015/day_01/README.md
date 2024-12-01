# Day 1 (2015)

`Not Quite Lisp` ([prompt](https://adventofcode.com/2015/day/1))

## Part 1

We just need the number of `(`s minus the number of `)`s so use `.count()` to count each and do the sum.

## Part 2

1. Start at floor 0. Iterate through the input using `enumerate()` to keep an index (`step`) and making sure we start at step 1 rather than the default of 0.

```python
    floor = 0
    for step, instruction in enumerate(self.input, start=1):
```

2. With each iteration, increment the floor by 1 for `(`, by -1 (i.e. decrease by 1) for `)` or else remain unchanged.

```python
        floor += 1 if instruction == "(" else -1 if instruction == ")" else 0
```

3. After each iteration, check if we've reached floor -1 and return the `step` if so.

```python
        if floor == -1:
            return step
```

4. If we reach the end of the input without reaching floor -1, raise an error.

```python
    raise ValueError("You didn't reach floor -1")
```
