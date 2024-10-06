#!/usr/bin/python3
import math

def print_factor(num):
    i = 1
    while i * i <= num:
        if (num % i == 0):
            factor = num // i
            print("{:d}={:d}*{:d}".format(num, factor, i))
            break
        i += 1


def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit()

    try:
        fl = open(argv[1], "r")
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
    else:
        while (True):
            ln = fl.readline()
            if (not ln):
                break
            ln = int(ln)
            print_factor(ln)

    f.close()


main()
