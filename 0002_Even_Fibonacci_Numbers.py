'''
def generate_fibonacci_up_to(max_value):
    fibs = [0, 1]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > max_value:
            break
        fibs.append(next_fib)
    return fibs

def find_fibonacci_pair(target_sum):
    fibs = generate_fibonacci_up_to(target_sum)
    fib_set = set(fibs)
    
    for fib in fibs:
        complement = target_sum - fib
        if complement in fib_set and complement != fib:
            return (fib, complement)
    return None

def get_even_fibonacci_numbers():
    fibs = generate_fibonacci_up_to(4000000)
    return [fib for fib in fibs if fib % 2 == 0]

target_sum = 4000000

pair_result = find_fibonacci_pair(target_sum)
print("Fibonacci pair that sums to 4,000,000:", pair_result)

even_fib_numbers = get_even_fibonacci_numbers()
print("\nEven Fibonacci numbers up to 4,000,000:", even_fib_numbers)

if len(even_fib_numbers) >= 2:
    if even_fib_numbers[-1] + even_fib_numbers[-2] == target_sum:
        print(f"\nSum of the last two even Fibonacci numbers equals the target sum: {target_sum}")
    else:
        print(f"\nSum of the last two even Fibonacci numbers does not equal the target sum: {target_sum} != {even_fib_numbers[-1]+even_fib_numbers[-2]}")
else:
    print("\nNot enough even Fibonacci numbers to perform the check.")
'''

#S=Fa+Fb
import math

def is_perfect_square(x):
    #Check if x is a perfect square
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci_number(n):
    """Check if n is a Fibonacci number
    A number n is a Fibonacci number if and only if
    one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square"""
    if n < 0:
        return False
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

print(is_fibonacci_number(3524578))

