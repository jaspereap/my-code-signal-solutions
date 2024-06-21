# ---
# dateAttempted: 2024-06-21
# time: 20:01
# url: https://app.codesignal.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo
# tags:
#   - arcade
# ---
def solution(n):
  if len(str(n)) == 1:
    return 0
  steps = 1
  while len(getSum(str(n))) != 1:
    n = getSum(str(n))
    steps += 1
  return steps
  
def getSum(s):
  currentSum = 0
  for c in s:
    currentSum += int(c)
  return str(currentSum)