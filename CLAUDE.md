# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Python repository for practicing data structures and algorithms (DSA) — stacks, queues, and similar topics. Each file is a standalone, self-contained script meant to be run independently rather than imported as part of a larger package.

## Running code

Run any individual file directly, e.g.:

```bash
python3 <filename>.py
```

There is no build step, package manager, or shared entry point — files do not depend on each other.

## Conventions

- New topics/exercises should be added as new, independently runnable `.py` files rather than being wired into a shared module or package structure.
- Keep each file self-contained (its own imports, its own `if __name__ == "__main__":` block or test calls) so it can be run on its own.
