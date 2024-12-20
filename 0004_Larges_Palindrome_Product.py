'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two-digit
numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.

'''
from measure_time import measure_time

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def find_largest_palindrome_optimized():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product
                factors = (i, j)
    return max_palindrome, factors

result, execution_time = measure_time(find_largest_palindrome_optimized)

largest_palindrome, factors = result

print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome}, which is the product of {factors[0]} and {factors[1]}.")
print(f"Time taken: {execution_time:.4f} milliseconds")