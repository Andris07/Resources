# Algorithm
def insertion_sort(array):
    for i in range(1, len(array)):
        temp = array[i]
        j = i - 1
        
        while j >= 0 and array[j] > temp:
            array[j+1] = array[j]
            j-=1
        array[j+1] = temp 

array = [9, 1, 8, 2, 7, 3, 6, 5, 4]
separator = ";"

print(f"unsorted:\t{separator.join(map(str, array))}")
insertion_sort(array)
print(f"sorted:\t\t{separator.join(map(str, array))}")