# ---
# dateAttempted: 2024-06-21
# time: 20:07
# url: https://app.codesignal.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
# tags:
# ---
def solution(inputArray, k):
  maxSum = sum(inputArray[:k])
  currentSum = maxSum
  for i in range(len(inputArray) - k):
    print(i)
    currentSum += inputArray[k + i]
    currentSum -= inputArray[i]
    if currentSum > maxSum:
      maxSum = currentSum
  return maxSum