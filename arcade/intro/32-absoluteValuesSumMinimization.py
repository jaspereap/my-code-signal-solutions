# ---
# dateAttempted: 2024-06-21
# time: 20:10
# url: https://app.codesignal.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq
# tags:
#   - arcade
# ---
import math

def solution(a):
  ans = 0
  smallest_diff_sum = math.inf
  for integer in a:
    diff_sum = 0
    for i in range(len(a)):
      diff_sum += abs(a[i] - integer)
    if diff_sum < smallest_diff_sum:
      smallest_diff_sum = diff_sum
      ans = integer
  return ans