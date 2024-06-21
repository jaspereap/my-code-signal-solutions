# ---
# dateAttempted: 2024-06-21
# time: 20:09
# url: https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R
# tags:
#   - arcade
# ---
def solution(inputArray, k):
  ans = []
  for i in range(len(inputArray)):
    if (i + 1) % k != 0:
      ans.append(inputArray[i])
  return ans