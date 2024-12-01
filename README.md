# Advent of Python

This is my attempt to solve the annual [Advent of Code](https://adventofcode.com/) puzzles, starting in 2024 and using [Python](https://www.python.org/). I'm not completely new to Python, but still consider myself a beginner. I will be trying to code in the most [Pythonic](https://peps.python.org/pep-0020/#the-zen-of-python) way my knowledge allows. I prefer [declarative programming vs imperative](https://dev.to/ruizb/declarative-vs-imperative-4a7l), so will err towards declarative where possible. I will use imperative where it fits best or where my skillset dictates. One of the things I like most about Python is that it's quite easy to mix paradigms and still produce expressive code.

I'm using [@xavdid](https://github.com/xavdid)'s [Advent of Code Python template](https://github.com/xavdid/advent-of-code-python-template) for this. I'm not aiming for speed with the solutions, but having the 'scaffolding' in place allows me to focus on the actual solution, rather than admin and boilerplate. The File Structure section below is taken directly from the `README` of the template repo.

I don't expect to get very far through a given puzzle year, but will be going back over each of the previous years.

## Solutions Completed

| Day | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
| --: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|   1 |      |      |      |      |      |      |      |      |      | \*\* |

## File Structure

<!-- generated with https://tree.nathanfriend.io/ -->

```
solutions/
├── ...
└── 2020/
    ├── day_01/
    │   ├── solution.py
    │   ├── input.txt
    │   ├── input.test.txt
    │   └── README.md
    ├── day_02/
    │   ├── solution.py
    │   ├── ...
    └── ...
```

- each year has a folder (`YYYY`)
- each day in that year (will eventually) have a folder (`day_NN`)

Each `day_NN` folder has the following files:

- `solution.py`, which has a `class Solution`. `./advent` expects both that filename and that class name exactly, so you shouldn't change them. See [Writing Solutions](#writing-solutions) for how the file is structured
- `input.txt` holds your individualized input from the AoC site. Make sure [not to share it publicly](https://old.reddit.com/r/adventofcode/wiki/troubleshooting/no_asking_for_inputs)!
- `input.test.txt` holds the example input from the prompt. It's read when the `--test-input` flag is used (see below). It also won't throw errors if the result doesn't match the [answer](#saving-answers). You can also do all your work in `input.txt`, but it's marginally less convenient
- `README.md` is a convenient place to take notes or explain your solution
