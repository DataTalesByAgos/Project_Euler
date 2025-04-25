from measure_time import measure_time

def sum_primes_below(n: int) -> int:
    """
    Returns the sum of all prime numbers less than n using the
    Sieve of Eratosthenes. We allocate a boolean array `is_prime`
    of size n, mark 0 and 1 as non-prime, then for each p from 2 up
    to sqrt(n) we sieve out multiples of p (starting at p*p). Finally
    we sum up all indices still marked as prime.
    
    First approach
    # Create a boolean list of length n, defaulting to True
    is_prime = [True] * n
    is_prime[0:2] = [False, False]   # 0 and 1 exceptions

    limit = int(n**0.5) + 1
    for p in range(2, limit):
        if is_prime[p]:
            # Mark off multiples of p, starting at p*p
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False

    # Sum and return all numbers that stayed marked as prime
    return sum(i for i, prime in enumerate(is_prime) if prime)
    """
    '''V2
    #Sums all primes < n using a memory-efficient sieve over odds only,
    #marking off multiples via slicing on a bytearray.
    
    We use a bytearray of length (n//2 - 1) to represent only odd numbers ≥3.
    Each slot i maps to the odd number 2*i+3, initialized to 1 (“potential prime”).
    When p=2*i+3 is prime, we zero out its odd multiples with one slice:
    sieve[start:size:p] = b"\x00"*count
    This in-place, C-level bulk assignment is much faster than a Python loop.
    '''
    if n <= 2:
        return 0

    # One slot per odd < n, excluding the '1'
    size = n // 2 - 1
    sieve = bytearray(b'\x01') * size

    limit = int(n**0.5)

    for i in range((limit - 3) // 2 + 1):
        if sieve[i]:
            p = 2*i + 3
            start = (p*p - 3) // 2
            count = ((size - 1) - start) // p + 1
            sieve[start : size : p] = b'\x00' * count

    total = 2
    for i, is_prime in enumerate(sieve):
        if is_prime:
            total += 2*i + 3

    return total

if __name__ == "__main__":
    LIMIT = 2_000_000
    result, exec_time = measure_time(sum_primes_below, LIMIT)
    print(f"The sum of all primes below {LIMIT:,} is: {result:,}")
    print(f"Execution time: {exec_time:.2f} ms")

#V1 = Execution time: 321.34 ms
#V2 = Execution time: 68.13 ms