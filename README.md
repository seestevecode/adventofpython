# Advent of Python

## Goals

... in no particular order

- Solving as many Advent of Code problems as I can, from 2015 to 2024
- Improving my knowledge of data structures and algorithms
- Improving my basic Python knowledge to intermediate
- Writing Pythonic code
- Trying to write code in a pseudo-functional way; brief, but readable
- Having fun and distracting myself from real life for a while!

## Solutions

| Day | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | Total |
| --: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | ----: |
|   1 | \*\* | \*\* | \*\* | \*\* | \*\* | \*\* | \*\* | \*\* | \*\* | \*\* |    10 |
|   2 | \*\* | \*\* | \*\* | \*\* |      |      |      | \*\* |      |      |     5 |
|   3 | \*\* | \*\* |      |      |      |      |      | \*\* |      |      |     3 |
|   4 | \*\* |      |      |      |      |      |      |      |      |      |     1 |
|   5 | \*\* |      |      |      |      |      |      |      |      |      |     1 |
|   6 | \*\* |      |      |      |      |      |      |      |      |      |     1 |
|   7 |      |      |      |      |      |      |      |      |      |      |       |
|   8 |      |      |      |      |      |      |      |      |      |      |       |
|   9 |      |      |      |      |      |      |      |      |      |      |       |
|  10 |      |      |      |      |      |      |      |      |      |      |       |
|  11 |      |      |      |      |      |      |      |      |      |      |       |
|  12 |      |      |      |      |      |      |      |      |      |      |       |
|  13 |      |      |      |      |      |      |      |      |      |      |       |
|  14 |      |      |      |      |      |      |      |      |      |      |       |
|  15 |      |      |      |      |      |      |      |      |      |      |       |
|  16 |      |      |      |      |      |      |      |      |      |      |       |
|  17 |      |      |      |      |      |      |      |      |      |      |       |
|  18 |      |      |      |      |      |      |      |      |      |      |       |
|  19 |      |      |      |      |      |      |      |      |      |      |       |
|  20 |      |      |      |      |      |      |      |      |      |      |       |
|  21 |      |      |      |      |      |      |      |      |      |      |       |
|  22 |      |      |      |      |      |      |      |      |      |      |       |
|  23 |      |      |      |      |      |      |      |      |      |      |       |
|  24 |      |      |      |      |      |      |      |      |      |      |       |
|  25 |      |      |      |      |      |      |      |      |      |      |       |
| Tot |  6   |  3   |  2   |  2   |  1   |  1   |  1   |  3   |  1   |  1   |    21 |

## Directory structure

```
. adventofcode/
├── adventofpython/ <--- THIS REPO
│   ├── event_2015/
│   │   ├── aoc2015_d01_solution.py
│   │   └── ...
│   ├── ...
│   ├── event_2024/
│   └── README.md
└── inputs/ <--- NOT INCLUDED IN THIS REPO
   ├── inputs_2015/
   │   ├── aoc2015_d01.txt
   │   └── ...
   ├── ...
   └── inputs_2024/
```

## Running a program

Each program should be run by piping the relevant input file to STDIN. This should work for both Linux and Windows.

e.g. running from the `adventofpython/` parent directory (YMMV):

```bash
python3 event_2015_d01_solution.py < ../inputs/inputs_2015/aoc2015_d01.txt
```
