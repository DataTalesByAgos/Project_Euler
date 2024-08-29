'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two-digit
numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.

'''
import time

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def find_largest_palindrome_optimized():
    max_palindrome = 0
    # Start from the largest 3-digit number and work downwards
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= max_palindrome:
                break  # Products will decrease after this
            if is_palindrome(product):
                max_palindrome = product
                factors = (i, j)
    return max_palindrome, factors

def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000
    return result, execution_time

result, execution_time = measure_time(find_largest_palindrome_optimized)

largest_palindrome, factors = result

print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome}, which is the product of {factors[0]} and {factors[1]}.")
print(f"Time taken: {execution_time:.4f} milliseconds")