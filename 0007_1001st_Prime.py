#What is the 10001st prime?

from measure_time import measure_time
from math import log, ceil

'Function to generate all prime numbers up to n'
def sieve_of_eratosthenes(limit):

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    
    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num * num, limit + 1, num):
                sieve[multiple] = False
    
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def nth_prime(n):
    'Find the nth prime number using an optimized sieve'
    if n == 1:
        return 2
    
    # Use the prime number theorem to estimate the upper limit for the nth prime.
    # Approximation: nth_prime(n) ≈ n * log(n) + n * log(log(n))
    limit = ceil(n * log(n) + n * log(log(n))) if n > 5 else 15  # A safe bound for small n.
    
    primes = sieve_of_eratosthenes(limit)
    
    if len(primes) >= n:
        return primes[n - 1]
    else:
        return nth_prime(n * 2)

if __name__ == "__main__":
    n = 10001

    result, execution_time = measure_time(nth_prime, n)

    print(f"The {n}th prime number is: {result}")
    print(f"Execution time: {execution_time:.2f} ms")

