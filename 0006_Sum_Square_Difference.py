from measure_time import measure_time

def sum_square_difference(n):
    sum_of_squares = sum(i**2 for i in range(1, n + 1))
    
    square_of_sum = sum(range(1, n + 1))**2
    
    return square_of_sum - sum_of_squares

if __name__ == "__main__":
    n = 100
    
    result, execution_time = measure_time(sum_square_difference, n)
    
    print(f"The difference between the sum of the squares and the square of the sum for the first {n} natural numbers is: {result}")
    print(f"Execution time: {execution_time:.2f} ms")
