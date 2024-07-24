'''
Problem 1
If we list all the natural numbers below 10 that are multiples 
of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''
import time

def measure_time(func, *args):
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time

def multiples():
    res = []
    
    for n in range(1,1000):
        if n % 3 == 0 or n % 5 == 0:
            res.append(n)
    return res

result, exec_time = measure_time(multiples)
print(f'The sum of all multiples of 3 or 5 below 1000 is: {sum(result)}')
print(f'Time taken: {exec_time:.6f} ms')

'''
#Math way

#Multiples 3 = [3,6,9..]
a = 3
d = 3
l = 999

l= a + d * (n - 1)

999 = 3 + 3 * (n - 1)
996 = 3 * (n - 1)
996 / 3 = (n - 1)
333 = n

'''  
##Sn = n/2 * ( a + l )
def sum_calc(multiple, n):
    num_terms = (n - 1) // multiple
    return multiple * num_terms * (num_terms + 1) // 2

result_3, exec_time_3 = measure_time(sum_calc, 3, 1000)
sum_3_multiples = result_3

result_5, exec_time_5 = measure_time(sum_calc, 5, 1000)
sum_5_multiples = result_5

result_15, exec_time_15 = measure_time(sum_calc, 15, 1000)
exclusion = result_15

final_result = sum_3_multiples + sum_5_multiples - exclusion
print(f'Multiples of 3 are: {sum_3_multiples}, multiples of 5 are: {sum_5_multiples}, final result: {final_result}')
print(f'Time taken by mathematical calculation for multiples of 3: {exec_time_3:.6f} ms')
print(f'Time taken by mathematical calculation for multiples of 5: {exec_time_5:.6f} ms')
print(f'Time taken by mathematical calculation for exclusion: {exec_time_15:.6f} ms')
total = exec_time_3 + exec_time_5 + exec_time_15
print(f'Total time: {total:.6f} ms')

if exec_time > total:
    speedup_percentage = ((exec_time - total) / exec_time) * 100
    print(f'Mathematical method is {speedup_percentage:.2f}% faster than the iterative method.')
else:
    slowdown_percentage = ((total - exec_time) / total) * 100
    print(f'Iterative method is {slowdown_percentage:.2f}% faster than the mathematical method.')