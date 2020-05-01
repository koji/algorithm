from functools import lru_cache
import time
@lru_cache(maxsize = 1000)
def fibonacci(n):
  if type(n) != int:
    raise TypeError('n must be int')
  if n < 1:
    raise TypeError('n must be a positive int')

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
