import random
import time

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return randomized_quicksort(less) + equal + randomized_quicksort(greater)

def deterministic_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    return deterministic_quicksort(less) + equal + deterministic_quicksort(greater)

# Performance comparison
def compare_quicksorts():
    input_sizes = [100, 1000, 5000, 10000]
    for size in input_sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]
        
        print(f"Input size: {size}")
        
        # Randomized Quicksort
        start = time.time()
        randomized_quicksort(arr)
        print(f"Randomized Quicksort: {time.time() - start:.5f} seconds")
        
        # Deterministic Quicksort
        start = time.time()
        deterministic_quicksort(arr)
        print(f"Deterministic Quicksort: {time.time() - start:.5f} seconds")
        print("-" * 40)

compare_quicksorts()
