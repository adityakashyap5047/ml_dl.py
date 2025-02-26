## When to use Multithreading

## I/O - bound tasks: Tasks that spend more time waiting for I/O expression (e.g. file operation, network requests.)
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Numbers: {i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

    # t = time.time()

    # print_numbers()
    # print_letter()

    # finished_time = time.time() - t

    # print(finished_time)

## Create 2 Threads
t1 = threading.Thread(target = print_numbers)
t2 = threading.Thread(target = print_letter)

t = time.time()
## Start the thread
t1.start()
t2.start()

# Wait for thread to complete
t1.join()
t2.join()

finished_time = time.time() - t
print(finished_time)