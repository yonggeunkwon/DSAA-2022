def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    sorted_array = arr
    return sorted_array

def search_matched_sum(arr, target):
    min_index = ()
    n = len(arr)
    print(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[i] + arr[j] == target:
                min_index = i, j
                break
            break
    return min_index

# bubbleSort 이용
def search_matched_sum(arr, target):
    min_index = ()
    print(arr)
    n = len(arr)
    arr = bubbleSort(arr)
    print(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[i] + arr[j] == target:
                min_index = i, j
                break
            break
    return min_index

arr = [5, 4, 2, 1]
# result1 = bubbleSort(arr)
# print(result1)
result = search_matched_sum(arr, 3)
print(result) 
# (2, 3)
        