#!/usr/bin/env python3
"""One-star review written by a house cat about its human.

Prints exactly one line and writes the same line to /output/entry.txt
(falling back to a local entry.txt if /output is not writable).
Pure standard library, no third-party dependencies.
"""

import os

LINE = (
    "One star. My human feeds me at 6am sharp, then has the nerve to "
    "sleep in on weekends like the bowl fills itself. "
    "Would not recommend this staff."
)


def main():
    print(LINE)
    for path in ("/output/entry.txt", "entry.txt"):
        try:
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(LINE + "\n")
            break
        except OSError:
            continue


if __name__ == "__main__":
    main()
