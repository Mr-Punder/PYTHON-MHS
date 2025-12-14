#!/usr/bin/env python3

import sys


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"nl: {filename}: No such file or directory", file=sys.stderr)
            sys.exit(1)
    else:
        lines = sys.stdin.readlines()

    for i, line in enumerate(lines, start=1):
        print(f"{i:>6}\t{line.rstrip()}")


if __name__ == "__main__":
    main()
