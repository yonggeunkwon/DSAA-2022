def merge_sort(unsorted_array):
    if len(unsorted_array) > 1:
        # print("un = ",unsorted_array)
        mid = len(unsorted_array) // 2
        left = unsorted_array[:mid]
        # print("l = ",left)
        right = unsorted_array[mid:]
        # print("r = ", right)

        merge_sort(left)
        merge_sort(right)
        
        i = j = k = 0
        # print("left = ",left)
        # print("right = ",right)
        # print("unsorted_array = ", unsorted_array)
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                unsorted_array[k] = left[i]
                i += 1
            else:
                unsorted_array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            unsorted_array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            unsorted_array[k] = right[j]
            j += 1 
            k += 1
        print("unsorted_array = ", unsorted_array)
        return unsorted_array

# def print_list(array1):
#     for i in range(len(array1)):
#         print(array1[i], end=" ")
#     # print()

    
from random import randint
array = [randint(1, 1000) for _ in range(10)]
print(array)
print(merge_sort(array))
# print(merge_sort(array))
# print(print_list(array))