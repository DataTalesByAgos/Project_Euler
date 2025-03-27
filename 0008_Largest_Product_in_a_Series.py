from measure_time import measure_time

number = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

''' 
old version:
def largest_product_in_series(n: int) -> int:
    max_product = 0
    for i in range(len(number) - n + 1):
        product = 1
        for j in range(n):
            product *= int(number[i + j])
        max_product = max(max_product, product)
    return max_product

This algorithm uses a "sliding window" of size n to find the greatest product efficiently.
Instead of recalculating the product from scratch at each step (O(n) per window, O(Nn) overall),
we update the product by removing the previous digit and adding the new one, keeping it in O(1).
This reduces the algorithm's complexity from O(Nn) to O(N), making it significantly faster.
(sliding window: 0.47ms vs  old version: 2.02ms)
76.23% faster
'''
def largest_product_in_series(n: int) -> int:
    max_product = 0
    current_product = 1
    zero_count = 0

    for i in range(n):
        digit = int(number[i])
        if digit == 0:
            zero_count += 1
        else:
            current_product *= digit

    if zero_count == 0:
        max_product = current_product

    for i in range(n, len(number)):
        new_digit = int(number[i])
        old_digit = int(number[i - n])

        if old_digit == 0:
            zero_count -= 1
        else:
            current_product //= old_digit

        if new_digit == 0:
            zero_count += 1
        else:
            current_product *= new_digit 

        if zero_count == 0:
            max_product = max(max_product, current_product)

    return max_product

if __name__ == "__main__":
    result, execution_time = measure_time(largest_product_in_series, 13)

    print(f"The greatest product of 13 adjacent digits is: {result}")
    print(f"Execution time: {execution_time:.2f} ms")
