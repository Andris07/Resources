# Algorithm
def merge_sort(array):
    length = len(array)

    if length <= 1: return

    middle = length // 2

    left_array = array[:middle]
    right_array = array[middle:]

    merge_sort(left_array)
    merge_sort(right_array)

    merge(left_array, right_array, array)

def merge(left_array, right_array, array):
    left_size = len(left_array)
    right_size = len(right_array)

    left_index = 0
    right_index = 0
    array_index = 0

    # Merge both halves while elements remain in both arrays
    while left_index < left_size and right_index < right_size:
        if left_array[left_index] < right_array[right_index]:
            array[array_index] = left_array[left_index]
            left_index+=1
        else:
            array[array_index] = right_array[right_index]
            right_index+=1

        array_index+=1
    
    # Copy remaining elements from the left half
    while left_index < left_size:
        array[array_index] = left_array[left_index]
        left_index+=1
        array_index+=1

    # Copy remaining elements from the right half
    while right_index < right_size:
        array[array_index] = right_array[right_index]
        right_index+=1
        array_index+=1

array = [8, 2, 5, 3, 4, 7, 6, 1]
separator = ";"

print(f"unsorted:\t{separator.join(map(str, array))}")
merge_sort(array)
print(f"sorted:\t\t{separator.join(map(str, array))}")