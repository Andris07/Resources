# Algorithm
def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        temp = array[i]
        array[i] = array[min_index]
        array[min_index] = temp

array = [8, 7, 9, 2, 3, 1, 5, 4, 6]
separator = ";"

print(f"unsorted:\t{separator.join(map(str, array))}")
selection_sort(array)
print(f"sorted:\t\t{separator.join(map(str, array))}")