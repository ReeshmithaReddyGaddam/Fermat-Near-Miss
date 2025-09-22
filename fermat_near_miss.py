"""
Fermat Near Miss Finder

Usage:
    python fermat_near_miss.py <n> <k>
Example:
    python fermat_near_miss.py 5 25
"""

import math
import argparse

def main():
    parser = argparse.ArgumentParser(description="Fermat Near Miss Finder")
    parser.add_argument("n", type=int, help="Exponent (3 <= n <= 11)")
    parser.add_argument("k", type=int, help="Upper bound for x and y (k > 10)")
    args = parser.parse_args()

    n, k = args.n, args.k

    if not (2 < n < 12):
        print("Invalid input. n must be between 3 and 11.")
        return

    if k <= 10:
        print("Invalid input. k must be greater than 10.")
        return

    smallest_relative_miss = float("inf")
    best_x = best_y = best_z = 0
    best_miss = 0

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            total = x ** n + y ** n
            z = round(total ** (1 / n))

            candidates = [(z, abs(total - z ** n)), (z + 1, abs(total - (z + 1) ** n))]
            chosen_z, miss = min(candidates, key=lambda item: item[1])

            relative_miss = miss / total
            print(f"x: {x}, y: {y}, z: {chosen_z}, Miss: {miss}, Relative Miss: {relative_miss:.7f}")

            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z, best_miss = x, y, chosen_z, miss

    print("\nBest Near Miss:")
    print(f"x: {best_x}, y: {best_y}, z: {best_z}, Miss: {best_miss}, Relative Miss: {smallest_relative_miss:.7f}")

if __name__ == "__main__":
    main()
