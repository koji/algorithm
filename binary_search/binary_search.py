def binary_search(list, item):
  low = 0
  high = len(list)-1

  while low <= high:
    mid = (low + high)
    guess = list[mid]
    if guess == item:
      return mid
    if guess > item:
      high = mid -1
    else:
      low = mid + 1
  return None

input_list = [1, 3, 5, 7, 9]
result1 = binary_search(input_list, 7)
result2 = binary_search(input_list, -1)
print(result1)
print(result2)
