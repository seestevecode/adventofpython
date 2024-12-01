# Day 1 (2017)

`Inverse Captcha` ([prompt](https://adventofcode.com/2017/day/1))

1. Create a helper function which will work for both Parts. Loop through each element of the input using a generator comprehension and the `enumerate` function to give us the index (`i`) as well as the value (`n`). For each, we check if the `i`th element is equal to the element that is `off` positions away. We apply the modulus function for the length of the sequence to ensure we 'wrap around' as needed. Sum the integers of the values that match.

```python
    return sum(int(n) for i, n in enumerate(seq) if seq[i] == seq[(i + off) % len(seq)])
```

2. Using the single function `solve` approach of the template, run the `captcha` function with an offset of 1 for Part 1, and an offset of half the length of the input for Part 2.

```python
    return captcha(self.input, 1), captcha(self.input, len(self.input) // 2)
```
