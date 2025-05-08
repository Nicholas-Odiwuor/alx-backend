# 0x00. Pagination

This project focuses on building a simple backend pagination system using Python and the `Popular_Baby_Names.csv` dataset. The objective is to efficiently paginate a dataset, returning indexed pages of data to simulate how real-world APIs handle large data collections.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Code must follow [pycodestyle](https://pypi.org/project/pycodestyle/) (version 2.5.*)
- All scripts should start with `#!/usr/bin/env python3`
- End all files with a new line
- All functions and modules must be documented with full sentences
- All functions must be type-annotated
- File lengths will be checked using `wc`

## Dataset

- `Popular_Baby_Names.csv` — a dataset of baby names used for pagination

## Features

- Server-like class with pagination methods
- Methods to get page and index ranges
- Resilient to changes in dataset (e.g., deletions)
- Handles edge cases (invalid inputs, out-of-range indices)

## Usage

Import and use the pagination functions/classes to fetch indexed pages from the dataset. Ensure to test with edge cases and validate output correctness.

## Author##
Nicholas Odiwuor
