#What is the largest prime factor of the number 600851475143 ?
#The prime factors of 13195 are 5, 7, 13, and 29
'''
# out of memory, you don't need to store all the primes haha :(
import math 

def find_primes(num):
    if num < 2:
        return []

    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False

    # Sieve of Eratosthenes
    len = int(math.sqrt(num)) + 1
    for i in range(2, len):
        if is_prime[i]:
            for j in range(i * i, num + 1, i):
                is_prime[j] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

print(find_primes(num_target))

For any prime number greater than 3, it can be shown that the number must be of the form 
6k±1 for some integer k. This is based on the fact that prime numbers cannot be divisible by 2 or 3.

'''
from measure_time import measure_time

def largest_prime_factor(n):
    largest = None
    
    while n % 2 == 0:
        largest = 2
        n //= 2

    while n % 3 == 0:
        largest = 3
        n //= 3

    i = 5
    while i * i <= n:
        while n % i == 0:
            largest = i
            n //= i
        while n % (i + 2) == 0:
            largest = i + 2
            n //= (i + 2)
        i += 6

    if n > 1:
        largest = n

    return largest

# num_target = 117
num_target = 600851475143

result, exec_time = measure_time(largest_prime_factor, num_target)

print(f"Largest prime factor of {num_target} is {result}")
print(f"Execution time: {exec_time:.6f} ms")
