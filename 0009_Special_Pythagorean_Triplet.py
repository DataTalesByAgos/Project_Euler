from measure_time import measure_time
'''
1st Approach:
This function finds the unique Pythagorean triplet (a, b, c) for which a + b + c equals a given total
(e.g., 1000) by iterating through possible values of a and b. The limits for a and b are chosen such that
a < sum_total/3 and b < sum_total/2 to ensure a valid triplet (with a < b < c). The value of c is computed
as c = sum_total - a - b, and the Pythagorean condition a^2 + b^2 == c^2 is checked. Once a valid triplet is found,
the function returns the product a * b * c

def special_pythagorean_triplet(sum_total: int) -> int:
    for a in range(1, sum_total // 3):
        for b in range(a + 1, sum_total // 2):
            c = sum_total - a - b
            if a * a + b * b == c * c:
                return a * b * c 
    return -1 

By using Euclid's formula, the algorithm is significantly improved compared to the brute-force approach.
Instead of iterating over all possible combinations of a and b and then computing c, Euclid's formula generates
a Pythagorean triplet directly from two integers, m and n (with m > n), using:
   a = k * (m^2 - n^2)
   b = k * (2 * m * n)
   c = k * (m^2 + n^2)

Moreover, given the condition a + b + c = sum_total, we can derive:
   k * 2 * m * (m + n) = sum_total
 which allows us to quickly check if a valid scaling factor k (an integer) exists for the pair (m, n).
 This mathematical approach reduces the number of iterations and computations by focusing only on those (m, n)
 pairs that can potentially yield the required triplet, making the algorithm both more elegant and efficient.
'''

def special_pythagorean_triplet(sum_total: int) -> int:
    for m in range(2, sum_total):
        for n in range(1, m):
            denominator = 2 * m * (m + n)
            if denominator > sum_total:
                continue  # Skip cases where the denominator exceeds sum_total
            if sum_total % denominator == 0:
                k = sum_total // denominator
                a = k * (m * m - n * n)
                b = k * (2 * m * n)
                c = k * (m * m + n * n)
                if a + b + c == sum_total:
                    return a * b * c
    return -1

if __name__ == "__main__":
    result, execution_time = measure_time(special_pythagorean_triplet, 1000)

    print(f"The product abc is: {result}")
    print(f"Execution time: {execution_time:.2f} ms")
