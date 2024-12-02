# Day 2 (2024)

`Red-Nosed Reports` ([prompt](https://adventofcode.com/2024/day/2))

The `parse` function is fairly standard and just turns the input - which is a block of lines of space-separated numbers - into a list of lists of integers.

```python
    return [list(map(int, line.split())) for line in input]
```

## Part 1

1. First we create a function to establish whether a report (list of integers) is safe.
2. For a given report, we create a list of paired numbers by using the `zip` function with the report and the report offset by one place. We then find the absolute difference between each of these pairs and assign it to `gaps`.

```python
    gaps = [abs(x - y) for x, y in zip(report, report[1:])]
```

3. To check if the report is ordered properly (safely), we check to see if it is either equal to the sorted version of itself or to the reverse-sorted version of itself.

```python
    is_ordered = report in [sorted(report), sorted(report, reverse=True)]
```

4. For the report to be safe, it must be ordered safely and all in `gaps` must be between 1 and 3, inclusive.

```python
    return is_ordered and all(1 <= gap <= 3 for gap in gaps)
```

5. To get the answer for the part, we just count how many reports/rows in the input are safe, using the `is_safe` function.

```python
    return sum(1 for report in parse(self.input) if is_safe(report))
```

## Part 2

1. For part 2, we create a separate function, `is_safe_dampened`, but we can re-use the `is_safe` function from part 1.
2. First we create a list of 'dampened' reports from the raw report, by iterating through each level and returning the report with that level missing.

```python
    dampened = [report[:level] + report[level + 1 :] for level in range(len(report))]
```

3. We then assert that the report is safe dampened if it is either safe 'undampened' or any of the dampened reports are safe.

```python
    return is_safe(report) or any(is_safe(dampened_rprt) for dampened_rprt in dampened)
```

4. Again, we use this function to count the number of reports that are safe if dampened.

```python
    return sum(1 for report in parse(self.input) if is_safe_dampened(report))
```
