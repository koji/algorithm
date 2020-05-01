import time
def fibonacci(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  elif n > 2:
    return fibonacci(n-1) + fibonacci(n-2)


start = time.time()
for i in range(1, 101):
  print(i, ":",  fibonacci(i))
elapsed_time = time.time() - start
print(elapsed_time)