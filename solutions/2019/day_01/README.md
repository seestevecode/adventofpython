# Day 1 (2019)

`The Tyranny of the Rocket Equation` ([prompt](https://adventofcode.com/2019/day/1))

1. Create a simple `fuel` function. This uses integer division (`//`) to divide by 3 and round down, then subtracts 2.

```python
    return mass // 3 - 2
```

2. Create a `complex_fuel` function using _recursion_. This has a 'base case' of returning 0 if the calculated fuel is 0 or less. In other cases, it returns the calculated fuel plus the complex fuel for the calculated fuel. This has the net effect of accumulating the fuel until there's no more to accumulate. E.g. For a mass of 14, `fuel` returns 2 so `complex_fuel` returns 2 plus the complex fuel for 2. Fuel for mass 2 is less than 0, so complex fuel returns 0 for a mass of 2. So the complex fuel for 14 is 2 (`fuel(14)`) + 0 (`complex_fuel(2)`) = 2.

```python
    return 0 if fuel(mass) <= 0 else fuel(mass) + complex_fuel(fuel(mass))
```

## Part 1

Sum the (simple) fuel function over each line in the input, after turning the mass to an integer.

## Part 2

Sum the complex fuel function over each line in the input, after turning the mass to an integer.
