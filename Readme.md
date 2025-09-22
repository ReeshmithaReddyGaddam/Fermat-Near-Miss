# Fermat Near Miss Finder

## Overview
This program explores near misses of Fermat's Last Theorem, taking inputs as **command-line arguments**.

## Installation
1. Clone the repository or download the files:
   ```bash
   git https://github.com/ReeshmithaReddyGaddam/Fermat-Near-Miss
   cd Fermat-Near-Miss
   ```

2. Ensure you have Python 3 installed.

## Usage
Run the script with two arguments:
```bash
python fermat_near_miss.py <n> <k>
```
- `<n>`: Exponent (3 ≤ n ≤ 11)
- `<k>`: Upper bound for x and y (k > 10)

## Example Run
```bash
python fermat_near_miss.py 5 22
```
_Output (partial):_
```
x: 10, y: 10, z: 13, Miss: 17651, Relative Miss: 0.0005921
...
Best Near Miss:
x: 14, y: 20, z: 24, Miss: 833, Relative Miss: 0.0000847
```

## Notes
- Uses integer arithmetic where possible.
- Runtime grows quadratically with k.
- No interactive inputs; values must be passed as arguments.
