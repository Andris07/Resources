# Algorithm
def quick_sort(array, start, end):
    if end <= start: return

    pivot = partition(array, start, end)

    quick_sort(array, start, pivot - 1)
    quick_sort(array, pivot + 1, end)
    
def partition(array, start, end):
    pivot = array[end]
    i = start - 1
    
    for j in range(start, end):
        if array[j] < pivot:
            i+=1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    
    i+=1
    temp = array[i]
    array[i] = array[end]
    array[end] = temp

    return i

array = [8, 2, 5, 3, 4, 7, 6, 1]
separator = ";"

print(f"unsorted:\t{separator.join(map(str, array))}")
quick_sort(array, 0, len(array) - 1)
print(f"sorted:\t\t{separator.join(map(str, array))}")