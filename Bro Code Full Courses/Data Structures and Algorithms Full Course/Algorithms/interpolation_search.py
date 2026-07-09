# Algorithm
def interpolation_search(array, value):
    low = 0
    high = len(array) - 1

    while value >= array[low] and value <= array[high] and low <= high:
        probe = low + (high - low) * (value - array[low]) // (array[high] - array[low])

        # specific edge-case: all values are the same in the array (throws ZeroDivisionError Exception if not handled)
        if array[high] == array[low]:
            if array[low] == value:
                return low
            break

        if array[probe] < value:
            low = probe + 1
        elif array[probe] > value:
            high = probe - 1
        else:
            return probe

    return -1

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9] evenly distributed array
array = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
index = interpolation_search(array, 256)

if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")