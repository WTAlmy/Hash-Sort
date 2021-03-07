#!/usr/bin/python3
import time
import random

NUM_INTS = 10000000 # 10 mil
MAX_NUMBER = 100000 # 100k

# Generate NUM_INTS random integers between 0 and MAX_NUMBER
nums = list()
for i in range(NUM_INTS):
  nums.append(random.randint(0, MAX_NUMBER))


# Hash Sort (n)
TIC = time.perf_counter()
hist = dict()

for i in range(MAX_NUMBER + 1):
  hist[i] = 0

for num in nums:
  hist[num] += 1

result = list()
for i in range(MAX_NUMBER):
  for n in range(hist.get(i,0)):
    result.append(i)
TOC = time.perf_counter()

# Hash Sort Results
print(TOC-TIC, "seconds")
print(result[0:100])


# Timsort (n log n)
TIC = time.perf_counter()
result = sorted(nums)
TOC = time.perf_counter()

# Timsort Results
print(TOC-TIC, "seconds")
print(result[0:100])
