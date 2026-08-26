# DSA

![Python](https://img.shields.io/badge/python-3-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)
![Made with love](https://img.shields.io/badge/made%20with-%E2%9D%A4-red)

Practice implementations of data structures and algorithms in Python — searching, sorting, stacks, queues, and similar topics.

## Structure

Each file is a standalone, self-contained script. Files do not import from or depend on each other, so you can run any file directly:

```bash
python3 <filename>.py
```

There is no build step, package manager, or shared entry point.

## Contents

| File                                   | Topic          |
| -------------------------------------- | -------------- |
| [linear-search.py](linear-search.py)   | Linear search  |
| [binary-search.py](binary-search.py)   | Binary search  |
| [selection-sort.py](selection-sort.py) | Selection sort |
| [bubble-sort.py](bubble-sort.py)       | Bubble sort    |
| [insertion-sort.py](insertion-sort.py) | Insertion sort |

## Conventions

- New topics/exercises are added as new, independently runnable `.py` files rather than wired into a shared module or package.
- Each file is self-contained: its own imports, and an `if __name__ == "__main__":` block or direct test calls.
