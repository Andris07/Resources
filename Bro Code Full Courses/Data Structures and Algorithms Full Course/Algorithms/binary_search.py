# Algorithm
def binary_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        middle = low + (high - low) // 2
        value = array[middle]

        if value < target:
            low = middle + 1
        elif value > target:
            high = middle - 1
        else:
            return middle
        
    return -1

array = list(range(1_000_000))
target = 777_777
index = binary_search(array, target)

if index != -1:
    print(f"Element found at index: {index}")
else:
    print(f"{target} not found")