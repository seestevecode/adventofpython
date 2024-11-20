# Advent of Python

## Completed

| Day | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 |
| --: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|   1 | \*\* | \*\* | \*\* | \*\* |      |      |      |      |      |      |
|   2 | \*\* | \*\* | \*\* |      |      |      |      |      |      |      |
|   3 | \*\* |      |      |      |      |      |      |      |      |      |
|   4 | \*\* |      |      |      |      |      |      |      |      |      |
|   5 | \*\* |      |      |      |      |      |      |      |      |      |
|   6 | \*\* |      |      |      |      |      |      |      |      |      |
|   7 |      |      |      |      |      |      |      |      |      |      |
|   8 |      |      |      |      |      |      |      |      |      |      |
|   9 |      |      |      |      |      |      |      |      |      |      |
|  10 |      |      |      |      |      |      |      |      |      |      |
|  11 |      |      |      |      |      |      |      |      |      |      |
|  12 |      |      |      |      |      |      |      |      |      |      |
|  13 |      |      |      |      |      |      |      |      |      |      |
|  14 |      |      |      |      |      |      |      |      |      |      |
|  15 |      |      |      |      |      |      |      |      |      |      |
|  16 |      |      |      |      |      |      |      |      |      |      |
|  17 |      |      |      |      |      |      |      |      |      |      |
|  18 |      |      |      |      |      |      |      |      |      |      |
|  19 |      |      |      |      |      |      |      |      |      |      |
|  20 |      |      |      |      |      |      |      |      |      |      |
|  21 |      |      |      |      |      |      |      |      |      |      |
|  22 |      |      |      |      |      |      |      |      |      |      |
|  23 |      |      |      |      |      |      |      |      |      |      |
|  24 |      |      |      |      |      |      |      |      |      |      |

<details>
    <summary><strong>Event 2015</strong> - 6 days - 12 stars</summary><br>

|                            Day | Puzzle                                 | Stars |
| -----------------------------: | :------------------------------------- | :---: |
| [1](/event_2015/aoc2015d01.py) | Not Quite Lisp                         | \*\*  |
| [2](/event_2015/aoc2015d02.py) | I Was Told There Would Be No Math      | \*\*  |
| [3](/event_2015/aoc2015d03.py) | Perfectly Spherical Houses in a Vacuum | \*\*  |
| [4](/event_2015/aoc2015d04.py) | The Ideal Stocking Stuffer             | \*\*  |
| [5](/event_2015/aoc2015d05.py) | Doesn't He Have Intern-Elves For This? | \*\*  |
| [6](/event_2015/aoc2015d06.py) | Probably a Fire Hazard                 | \*\*  |

</details>

<details>
    <summary><strong>Event 2016</strong> - 2 days - 4 stars</summary><br>

|                            Day | Puzzle                | Stars |
| -----------------------------: | :-------------------- | :---: |
| [1](/event_2016/aoc2016d01.py) | No Time for a Taxicab | \*\*  |
| [2](/event_2016/aoc2016d02.py) | Bathroom Security     | \*\*  |

</details>

<details>
    <summary><strong>Event 2017</strong> - 2 days - 4 stars</summary><br>

|                            Day | Puzzle              | Stars |
| -----------------------------: | :------------------ | :---: |
| [1](/event_2017/aoc2017d01.py) | Inverse Captcha     | \*\*  |
| [2](/event_2017/aoc2017d02.py) | Corruption Checksum | \*\*  |

</details>

<details>
    <summary><strong>Event 2018</strong> - 1 day - 2 stars</summary><br>

|                            Day | Puzzle              | Stars |
| -----------------------------: | :------------------ | :---: |
| [1](/event_2018/aoc2018d01.py) | Chronal Calibration | \*\*  |

</details>
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
