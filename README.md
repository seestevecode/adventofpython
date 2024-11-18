# Advent of Python

## File Structure

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
