# Day 1 (2024)

`Historian Hysteria` ([prompt](https://adventofcode.com/2024/day/1))

1. The `parse` function aims to take the input, which is read as a `list[str]`, and output a `list[list[int]]`. There will only ever be two lists, but returning as a list of lists is more flexible.

```python
def parse(input: list[str]) -> list[list[int]]:
```

2. We use a list comprehension to loop through the input lines. For each, we split (using default delimiters) to get a list of strings. We then `map` the `int` function over the list of strings. This returns a list of Map objects, but we don't need to turn this into a list of lists at this point, as the next line will do that.

```python
    parsed_lines = [map(int, line.split()) for line in input]
```

3. Here we are trying to _transpose_ the list of mapped integer pairs to return a list (pair) of lists of integers. We use the `*` operator to unpack the output from the last line. We then use `zip` to repack them in the 'flipped' way that we want. Finally, we use `sorted` to ensure the returned lists are in ascending order. This isn't needed for Part Two, but is needed for Part One and having them sorted won't cause any issues with Part Two.

```python
    return [sorted(list_of_nums) for list_of_nums in zip(*parsed_lines)]
```

## Part 1

1. We again combine the use of `*` and `zip` to transpose the output of the `parse` function back to a list of paired numbers - although this time, I'm using `tuple` to return a tuple of integers for each line. The only difference between the output of this line and the original input is that here the numbers in each 'column' are sorted.

```python
    list_of_pairs = [tuple(x) for x in zip(*parse(self.input))]
```

2. We finish Part 1 by using a list comprehension (technically, it's a generator comprehension) to loop through the pairs, find the absolute difference and sum over all pairs.

```python
    return sum(abs(pair[0] - pair[1]) for pair in list_of_pairs)
```

## Part 2

1. This time, we want to keep the output of the `parse` function as two separate lists. Again, it doesn't matter that they're sorted; that won't affect this part. We assign the lists to the `left` and `right` variables respectively.

```python
    left, right = parse(self.input)
```

2. Another list/generator comprehension, this time we loop through the `left` list and multiply each `num` by the number of times it appears in `right`. Summing this multiplication for each `num` in the left list gives us our answer.

```python
    return sum(num * right.count(num) for num in left)
```
