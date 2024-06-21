# ---
# dateAttempted: 2024-06-21
# time: 20:04
# url: https://app.codesignal.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2
# tags:
#   - arcade
# ---
def solution(value1, weight1, value2, weight2, maxW):
  if weight1 + weight2 > maxW:
    if weight1 > maxW and weight2 > maxW:
      return 0
    if weight1 <= maxW and weight2 > maxW:
      return value1
    if weight2 <= maxW and weight1 > maxW:
      return value2
    if value1 > value2:
      return value1
    else:
      return value2
  return value1 + value2