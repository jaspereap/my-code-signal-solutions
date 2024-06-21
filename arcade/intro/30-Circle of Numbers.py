# ---
# dateAttempted: 2024-06-21
# time: 20:11
# url: https://app.codesignal.com/arcade/intro/level-7/vExYvcGnFsEYSt8nQ
# tags:
#   - arcade
# ---
def solution(n, firstNumber):
  if (firstNumber + n/2) >= n:
    return (firstNumber + n/2) - n
  return firstNumber + n/2