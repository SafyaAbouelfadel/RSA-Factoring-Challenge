#!/usr/bin/python3

def print_factor(num):
    if num < 2:
        return  # No factors for numbers less than 2

    for a in range(2, int(num**0.5) + 1):  # Start from 2 and check up to sqrt(num)
        if num % a == 0:
            factor = num // a
            print("{:d} = {:d} * {:d}".format(num, factor, a))
            return
    print("{:d} = {:d} * 1".format(num, num))  # If no factors found, it must be prime


def main():
    from sys import argv, exit, stderr

    if len(argv) != 2:
        stderr.write("Usage: ./factors <file>\n")
        exit(1)

    try:
        with open(argv[1], "r") as f:
            for ln in f:
                ln = ln.strip()
                try:
                    num = int(ln)
                    print_factor(num)
                except ValueError:
                    stderr.write("Invalid number: {}\n".format(ln))
    except FileNotFoundError:
        stderr.write("Could not find file: {}\n".format(argv[1]))
        exit(1)


if __name__ == "__main__":
    main()
