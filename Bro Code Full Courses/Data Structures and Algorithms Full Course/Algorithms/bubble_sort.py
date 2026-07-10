# Algorithm
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if (array[j] > array[j+1]):
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

array = [9, 1, 8, 2, 7, 3, 6, 4, 5]
separator = ";"

print(f"unsorted:\t{separator.join(map(str, array))}")
bubble_sort(array)
print(f"sorted:\t\t{separator.join(map(str, array))}")