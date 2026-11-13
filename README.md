# Decoding and Encoding Algorithm

A matrix cipher in Python, written as an undergraduate programming assignment. Encoding turns letters into numbers (`A` is 1, `Z` is 26, space is 27), splits them into blocks and multiplies each block by a square key matrix. Decoding inverts the key with Gauss-Jordan elimination and maps the numbers back to letters.

## Run

```bash
python assignment4.py enc key.txt plain.txt cipher.txt
python assignment4.py dec key.txt cipher.txt plain.txt
```

The arguments are the operation (`enc` or `dec`), the key file, the input file and the output file.

## Input

- **Key file:** an n x n matrix of integers, separated by commas, one row per line.
- **Input for `enc`:** letters and spaces only, with no line break. Lower case is converted to upper case and the text is padded with spaces to a multiple of n.
- **Input for `dec`:** the comma-separated numbers written by `enc`.

The key and input file names must end in `txt`. An unknown operation, a missing or empty file and an invalid character each stop the program with a one-line error message.

## Requirements

Python 3, standard library only.
