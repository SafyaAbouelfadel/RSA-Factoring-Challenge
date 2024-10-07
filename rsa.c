#include <stdio.h>
#include <math.h>

/* Function to check if a number is prime */
int is_prime(unsigned long long num) {
	if (num <= 1)
		return 0;
	if (num <= 3)
		return 1;
	if (num % 2 == 0 || num % 3 == 0)
		return 0;
	for (unsigned long long i = 5; i * i <= num; i += 6) {
		if (num % i == 0 || num % (i + 2) == 0)
			return 0;
	}
	return 1;
}

/* Function to factorize n into p and q */
void find_factors(unsigned long long n) {
	unsigned long long p, q;
	/* Trial division starting from the smallest prime */
	for (p = 2; p <= sqrt(n); p++) {
		if (n % p == 0) {
			q = n / p;
			/* Check if both p and q are prime */
			if (is_prime(p) && is_prime(q)) {
				printf("%llu = %llu * %llu\n", n, p, q);
				return;
			}
		}
	}
	/* If no factors are found */
	printf("Factors not found\n");
}

int main(int argc, char *argv[]) {
	if (argc != 2) {
		fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
		return 1;
	}

	FILE *file = fopen(argv[1], "r");
	if (!file) {
		fprintf(stderr, "Error: could not open file %s\n", argv[1]);
		return 1;
	}

	unsigned long long n;
	fscanf(file, "%llu", &n);
	fclose(file);

	find_factors(n);
	return 0;
}
