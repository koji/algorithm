def findMin(arr):
    min = arr[0]
    min_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index


def selectionSort(arr):
    result = []
    for i in range(len(arr)):
        min = findMin(arr)
        result.append(arr.pop(min))
    return result

inputArr = [5, 3, 6, 2, 10]
print(selectionSort(inputArr))
