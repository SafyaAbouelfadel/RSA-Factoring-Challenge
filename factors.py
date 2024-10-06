#!/usr/bin/python3
import math

def print_factor(num):
    a = 2
    if (num % a == 0):
        print("{:d}={:d}*{:d}".format(num, num // a, a))
    a = 3
    while a < num // 2:
        if num % a == 0:
            print("{}={}*{}".format(num, num // a, a))
            break
        a = a + 2
        if a == (num // 2) + 1:
            print("{}={}*{}".format(num, num, 1))

def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit()

    try:
        f = open(argv[1], "r")
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
    else:
        while (True):
            ln = f.readline()
            if (not ln):
                break
            ln = int(ln)
            print_factor(ln)

    f.close()


main()
