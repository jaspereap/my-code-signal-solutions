# ---
# dateAttempted: 2024-06-21
# time: 20:06
# url: https://app.codesignal.com/arcade/intro/level-9/xHvruDnQCx7mYom3T
# tags:
#   - arcade
# ---
def solution(upSpeed, downSpeed, desiredHeight):
  days = 0
  height = 0
  while height <= desiredHeight:
    height += upSpeed
    days += 1
    if height >= desiredHeight:
      return days
    height -= downSpeed
  return days