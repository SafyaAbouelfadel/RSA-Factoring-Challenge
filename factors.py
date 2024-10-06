#!/usr/bin/python3
import math
import random
from sys import argv, exit, stderr

# Pollard's Rho algorithm to find a non-trivial factor
def pollards_rho(n):
    if n % 2 == 0:
        return 2
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    g = 1

    def f(x, n, c):
        return (x * x + c) % n

    while g == 1:
        x = f(x, n, c)
        y = f(f(y, n, c), n, c)
        g = math.gcd(abs(x - y), n)
    return g

# Function to print the factors of a number
def print_factor(num):
    if num < 2:
        return  # No factors for numbers less than 2

    # Set threshold for using Pollard's Rho
    threshold = 10**6  # Adjust this value as needed

    # Quick check for small factors
    if num < threshold:
        # Check for small factors
        if num % 2 == 0:
            print(f"{num}={num // 2}*2")
            return
        
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                other_factor = num // i
                print(f"{num}={other_factor}*{i}")
                return

    # If the number is large or no factors found, use Pollard's Rho
    factor = pollards_rho(num)
    if factor != num:
        print(f"{num}={num // factor}*{factor}")
    else:
        # If still no factor found, it's prime
        print(f"{num}={num}*1")  # Here, keep this case for primes

def main():
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
                    stderr.write(f"Invalid number: {ln}\n")
    except FileNotFoundError:
        stderr.write(f"Could not find file: {argv[1]}\n")
        exit(1)

if __name__ == "__main__":
    main()

