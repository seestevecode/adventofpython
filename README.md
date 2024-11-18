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
