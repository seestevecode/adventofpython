# Day 1 (2020)

`Report Repair` ([prompt](https://adventofcode.com/2020/day/1))

1. This solution uses the `combinations` function from the `itertools` library, which gives all non-repeating combinations of a specified size from a specified iterable. It also uses the `prod` function from the `math` library, which multiples all elements in an iterable.

```python
    from itertools import combinations
    from math import prod
```

2. We start by looping through all combinations of `combo_size` elements of the list of elements turned to integers.

```python
    for combo in combinations([int(num) for num in input], combo_size):
```

3. For each `combo`, we check if the elements sum to 2020 and, if they do, we return their product.

```python
        if sum(combo) == 2020:
            return prod(combo)
```

4. We raise an error if we get to the end of the combinations without meeting our criteria.

```python
    raise ValueError("You didn't find the right combo")
```

5. We then run the function for 2-element combos and 3-element combos, for parts 1 and 2 respectively.

```python
    return find_combo(self.input, 2), find_combo(self.input, 3)
```
