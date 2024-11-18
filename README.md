# Advent of Python

## Completed

| Day |               2015               | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
| --: | :------------------------------: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|   1 | [Yes](/event_2015/aoc2015d01.py) | Yes  |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   2 |               Yes                | Yes  |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   3 |               Yes                |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   4 |               Yes                |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   5 |               Yes                |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   6 |               Yes                |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   7 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   8 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|   9 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  10 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  11 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  12 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  13 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  14 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  15 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  16 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  17 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  18 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  19 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  20 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  21 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  22 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  23 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |
|  24 |                -                 |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |  -   |

## Directory Structure

- One folder per year, e.g. `event_2015/`
- One program per day, e.g. `event_2015/aoc2015d01.py`
- Inputs sit outside repository in a sibling directory, `inputs/`, that has the same structure as the repo.
- Input files have the same name as the Python file, but with no extension.

```
.
├── inputs/                  << NOT PART OF REPO
│   ├── event_2015/
│   │   ├── aoc2015d01
│   │   └── ...
│   ├── event_2016/
│   └── ...
├── python/                  << THIS REPO
│   ├── event_2015/
│   │   ├── aoc2015d01.py
│   ├── event_2016/
│   ├── ...
│   ├── template.py
│   └── utils.py
```

## Setup

1. (Recommended) Create a parent folder to hold all Advent of Code work. This can have further sub-directories for other languages that will still be able to access the same inputs.
2. Create at least `inputs/` and `python/` subdirectories, as above, and navigate to the `python/` directory.
3. Create a virtual environment at the top-level. You may need to use a different syntax, i.e. not `python3.13` but it will be similar. The `--prompt="aoc"` is optional but can be configured to show in your command line when you are in an active virtual environment.

```bash
python3.13 -m venv .venv --prompt="aoc"
```

4. Activate the virtual environment. Your shell can be configured to auto-activate and deactivate as you navigate to and from directories with a venv in them, but it is up to you to find this out if you want to.

```bash
source .venv/bin/activate
```
