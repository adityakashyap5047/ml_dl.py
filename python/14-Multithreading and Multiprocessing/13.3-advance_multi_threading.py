### Multithreading with Thread Pool Executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_numbers(number):
    time.sleep(2)
    return f"Numbers: {number}"

numbers = [1, 2, 3, 4, 5, 4, 5, 6, 9, 13, 34, 98]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_numbers, numbers)

    # for result in results:
    #     print(result)         # This will print the result in the order they are completed

for result in results:
    print(result)       # This will print the result when the loop is completed