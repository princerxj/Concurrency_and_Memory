### Multithreading 

## When to use 
# - I/O Bound Tasks - Tasks that spend more time waiting for I/O opeartions (example - file operations)
# - Concurrent Execution - Multiple operations concurrently 

import threading
import time

def print_numbers() :
    for i in range(5):
        time.sleep(2)
        print(f"Number : {i}")

def print_letter() :
    for letter in "abcde":
        time.sleep(2)
        print(f'Letter : {letter}')

##Create two threads 
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
#Start the thread
t1.start()
t2.start()

##wait for the threads to complete
t1.join()
t2.join()
finished_time = time.time() - t
print(finished_time)