from math import isqrt
from functools import lru_cache
from measure_time import measure_time

"""
Not sure if this is the best approach, but here’s how I tried to solve it.

So the idea was to find the *first* triangle number that has more than 500 divisors.
I thought I’d just generate triangle numbers and count their divisors one by one, 
but wow, that was slow. Way too slow actually.

Eventually I remembered that n and n+1 are always coprime, so maybe I could split them 
and factor separately depending on whether n is odd or even. That made things simpler.
Kinda confusing at first, but I got used to it.

The divisor counting part is based on the whole prime factor thing, like if 
you have a^x * b^y then it’s (x+1)(y+1)...

I also added caching cause Python lets you do that with lru_cache – super useful actually.
And I made a sieve to generate primes cause I didn’t want to check divisibility manually.

"""

def get_some_primes(limit: int) -> list[int]:
    flags = [True] * (limit + 1)
    flags[0] = flags[1] = False
    for i in range(2, isqrt(limit) + 1):
        if flags[i]:
            for j in range(i * i, limit + 1, i):
                flags[j] = False
    return [i for i, is_prime in enumerate(flags) if is_prime]

PRIMES = get_some_primes(10_000)  # probably more than needed but whatever

@lru_cache(maxsize=None)
def divisors_of(num: int) -> int:
    result = 1
    leftover = num  # keeping this separate helps me think
    for p in PRIMES:
        if p * p > leftover:
            break
        count = 0
        while leftover % p == 0:
            leftover //= p
            count += 1
        if count > 0:
            result *= (count + 1)
    if leftover > 1:
        result *= 2  # leftover is a prime
    return result

def triangle_divisors(n: int) -> int:
    # I split them like this depending on odd/even
    if n % 2 == 0:
        a = n // 2
        b = n + 1
    else:
        a = n
        b = (n + 1) // 2
    return divisors_of(a) * divisors_of(b)

def first_big_triangle(limit: int) -> int:
    n = 1
    while True:
        d = triangle_divisors(n)
        if d > limit:
            return n * (n + 1) // 2
        n += 1

if __name__ == "__main__":
    result, elapsed = measure_time(first_big_triangle, 500)
    print(f"First triangle number with >500 divisors is: {result}")
    print(f"Took around {elapsed:.2f} ms, give or take.")
