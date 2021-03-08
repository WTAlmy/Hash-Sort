#!/usr/bin/python3
import time
import random
import numpy as np

NUM_INTS =   16777216 # 2^24
MAX_NUMBER =    65536 # 2^16

# Generate NUM_INTS random integers between 0 and MAX_NUMBER
nums = list()
for i in range(NUM_INTS):
  nums.append(random.randint(0, MAX_NUMBER))


# Numpy Array Sort
TIC = time.perf_counter()
hist = np.bincount(nums)

result = list()
for i in range(MAX_NUMBER):
  for n in range(hist[i]):
    result.append(i)
TOC = time.perf_counter()

# Numpy Array Sort Results
print(TOC-TIC, "seconds")
print(result[0:100])


# Hash Sort (n)
TIC = time.perf_counter()
hist = dict()

for i in range(MAX_NUMBER + 1):
  hist[i] = 0

for num in nums:
  hist[num] += 1

result = list()
for i in range(MAX_NUMBER):
  for n in range(hist[i]):
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
