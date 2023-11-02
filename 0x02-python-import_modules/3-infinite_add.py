#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) <= 1:
        return


result = 0
for arg in sys.argv[1:]:
    result += int(arg)
print(f"{result}")
if __name__ == "__main__":
    main()
