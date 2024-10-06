#!/usr/bin/python3
import math

def print_factor(num):
    a = 2
    if num % a == 0:
        print("{:d}={:d}*{:d}".format(num, num // a, a))
        return
    a = 3
    limit = math.isqrt(num)  # Efficient square root for large numbers
    while a <= limit:
        if num % a == 0:
            print("{:d}={:d}*{:d}".format(num, num // a, a))
            return
        a += 2
    # No factor found, so print the identity factorization
    print("{:d}={:d}*1".format(num, num))

def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit(1)

    try:
        with open(argv[1], "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    ln = int(line)  # Ensure it's a valid integer
                    print_factor(ln)
    except FileNotFoundError:
        stderr.write("Could not find file {}, not exist\n".format(argv[1]))
        exit(1)
    except ValueError:
        stderr.write("Invalid number format in file\n")
        exit(1)

if __name__ == "__main__":
    main()
