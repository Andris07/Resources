# Algorithm
def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[min] > array[j]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp

array = [8, 7, 9, 2, 3, 1, 5, 4, 6]
separator = ";"

print(f"unsorted:\t{separator.join(map(str, array))}")
selection_sort(array)
print(f"sorted:\t\t{separator.join(map(str, array))}")