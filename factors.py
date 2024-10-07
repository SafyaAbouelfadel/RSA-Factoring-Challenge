import sys

def factorize(n):
    """Returns the first factor pair (p, q) such that n = p * q."""
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i, n // i
    return n, 1  # In case n is prime (though not necessary for this task)

def main(file_path):
    """Reads numbers from the file and factorizes each."""
    try:
        with open(file_path, 'r') as file:
            for line in file:
                n = int(line.strip())
                p, q = factorize(n)
                print(f"{n}={q}*{p}")
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except ValueError:
        print("Error: The file contains non-integer values.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
    else:
        main(sys.argv[1])
