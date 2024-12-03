# Day 3 (2024)

`Mull It Over` ([prompt](https://adventofcode.com/2024/day/3))

Here come the regular expressions ...

## Part 1

1. First find all the instances of "mul(xxx,yyy)" in the input. The return value `hits` is a list of tuples, containing the digits (as strings) that we captured.
   - `mul\(` finds the literal string "mul(" (the `\` is an escape character as `(` is a reserved character in regex).
   - `(\d{1,3})` finds a digit (`\d`) of length 1 to 3 and captures it due to the parentheses - note the lack of escape characters for these.
   - `,` finds the literal comma.
   - `(\d{1,3})` finds and captures another number with 1 to 3 digits.
   - `\)` finds the closing literal parenthesis.

```python
    hits = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", self.input)
```

2. With our list of stringified integers, we simply use a comprehension to loop through, cast them as `int`, multiply and sum.

```python
    return sum(int(a) * int(b) for a, b in hits)
```

## Part 2

> I tried hard to make this work with regex lookahead and/or lookbehind, but failed. As I wanted to get something out in the same day, I cheated and leaned on [@xavdid's blog post solution](https://advent-of-code.xavd.id/writeups/2024/day/3/). I will come back to it after learning more about regex, to see if my initial idea is even possible,

_NB I promise I did Part 1 unaided before I looked at any other solutions!_
