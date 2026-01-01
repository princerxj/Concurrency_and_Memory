'''
Real World Example : Multiprocessing for the CPU-bound tasks 
Scenario: Factorial Calculation 
Factorial Calculations, especially for the large numbers,
involve significant computational work. Multiprocessing can be used to distribute the workload 
across multiple CPU cores, improving performance.
'''

import multiprocessing
import math
import sys
import time 

# Increase the maximum number of digits for integer conversion 
sys.set_int_max_str_digits(100000)

## function to compute the factorial of a given number 
def compute_my_factorial(num) :
    print(f"Compute the factorial of {num}")
    result = math.factorial(num)
    print(f"Factorial of {num} is {result}")
    return result

if __name__ == "__main__" :
    numbers = [5000, 6000, 7000, 8000]

    start_time = time.time()

    ##Create  a pool of worker processes 
    with multiprocessing.Pool() as pool :
        results = pool.map(compute_my_factorial, numbers)

    end_time = time.time()

    print(f"Results : {results}")
    print(f"Time taken : {end_time - start_time} seconds")