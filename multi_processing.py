##This allows to make Processes that run in parallel 
### Used in CPU-Bound Tasks thar are heavy on CPU usage
## Parallel Execution - Multiple Cores of the CPU

import multiprocessing
import time 

def square_numbers() :
    for i in range(5) :
        time.sleep(1)
        print(f"Square is : {i ** 2}")

def cube_numbers() :
    for i in range(5) :
        time.sleep(1.5)
        print(f"Cube is : {i * i * i}")

if __name__ == "__main__":

    ## Create two processes 
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()

    ### Start the process 
    p1.start()
    p2.start()

    ##Wait for the process toget completed
    p1.join()
    p2.join()

    finished_time = time.time() - t
    print(finished_time)