'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two-digit
numbers is 9009 = 91 x 99

Find the largest palindrome made from the product of two 3-digit numbers.

'''

def is_palindrome(num):
    s = str(num)
    return s == s[::-1]

def find_largest_palindrome():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
                factors = (i, j)

    return max_palindrome, factors

largest_palindrome, factors = find_largest_palindrome()
print(f"The largest palindrome made from the product of two 3-digit numbers is {largest_palindrome}, which is the product of {factors[0]} and {factors[1]}.")
