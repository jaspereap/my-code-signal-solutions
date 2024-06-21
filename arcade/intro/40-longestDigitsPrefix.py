# ---
# dateAttempted: 2024-06-21
# time: 20:03
# url: https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3
# tags:
#   - arcade
# ---
def solution(inputString):
  for char in range(len(inputString)):
      if not inputString[char].isdigit():
          return inputString[:char]
  return inputString