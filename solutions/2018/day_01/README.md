# Day 1 (2018)

`Chronal Calibration` ([prompt](https://adventofcode.com/2018/day/1))

Create a simple `parse` function to return the input with each line turned to an integer.

## Part 1

Simply sum the parsed input.

## Part 2

1. Create an empty set to retain the seen values of frequency.

```python
    seen = set()
```

2. There's a lot going on here. We're using two functions, `accumulate` and `cycle` from the `itertools` library. `cycle` loops through the parsed input indefinitely, returning to the beginning when reaching the end. `accumulate` cumulatively sums the values as it goes. E.g. `accumulate(cycle([1, 2, 3]))` returns `[1, 3, 6, 7, 9, 12, 13, ...]`.

```python
    for frequency in accumulate(cycle(parse(self.input))):
```

3. With each iteration, if the frequency as already been seen, return it as the answer.

```python
        if frequency in seen:
            return frequency
```

4. If we get to this stage, i.e. the frequency wasn't seen, add it to the set of seen frequencies.

```python
        seen.add(frequency)
```

5. This is mainly just to please the linter.

```python
    raise ValueError("You didn't reach the same frequency twice")
```
