import time

def print_time(start, end):
    print(f"Recursive Binary Search Start Time: {start}")
    print(f"Recursive Binary Search End Time:   {end}")
    print(f"Time taken: {end - start:.6f} seconds")

def recursive_binary_search(arr, target, low, high, start_time=None):
    if start_time is None:
        start_time = time.time()

    if low > high:
        end_time = time.time()
        print_time(start_time, end_time)
        return -1

    mid = (low + high) // 2
    if arr[mid] == target:
        end_time = time.time()
        print_time(start_time, end_time)
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high, start_time)
    else:
        return recursive_binary_search(arr, target, low, mid - 1, start_time)

arr = list(range(100000))
target = 99999
index = recursive_binary_search(arr, target, 0, len(arr) - 1)

print(f"Element found at index: {index}")
