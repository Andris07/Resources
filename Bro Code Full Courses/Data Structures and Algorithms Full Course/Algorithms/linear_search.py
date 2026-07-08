# Algorithm
def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i

    return -1

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
index = linear_search(array, 1)

if index != -1:
    print(f"Element found at index: {index}")
else:
    print("Element not found")