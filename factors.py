#!/usr/bin/python3
import math

def print_factor(num):
    i = 1
    while i * i <= num:
        if num % i == 0:
            factor = num // i
            print("{:d} = {:d} * {:d}".format(num, factor, i))
            break
        i += 1


def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit(1)

    try:
        with open(argv[1], "r") as fl:
            for line in fl:
                try:
                    ln = int(line.strip())
                    print_factor(ln)
                except ValueError:
                    stderr.write("Invalid integer in file: {}\n".format(line.strip()))
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
        exit(1)


if __name__ == "__main__":
    main()

