from math import gcd
from functools import reduce
from measure_time import measure_time

def lcm(a, b):
    return a * b // gcd(a, b)

def smallest_multiple():
    return reduce(lcm, range(1, 21))

result, execution_time = measure_time(smallest_multiple)
print(f"Smallest multiple: {result}")
print(f"Execution time: {execution_time} seconds")
