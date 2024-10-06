#!/usr/bin/python3
from sys import argv

with open(argv[1]) as f:
    for ln in f:
        n = int(ln)
        print("{:d}=".format(n), end="")
        if n % 2 == 0:
            print("{}*2".format(n//2))
            continue
        for a in range(3, n, 2):
            if n % a == 0:
                factor = n//a
                for k in range(3, factor, 2):
                    if factor % k == 0 or a % k == 0:
                        break
                print("{}*{}".format(factor, a))
                break
