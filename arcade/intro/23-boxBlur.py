# ---
# dateAttempted: 2024-06-09
# time: 13:02
# url: https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP/drafts
# tags:
#   - arcade
#   - array
# ---

def solution(image):
  rows = len(image)
  cols = len(image[0])
  
  blurred = []
  
  for i in range(1, rows - 1):
    blurred_row = []
    for j in range(1, cols - 1):
      sum = 0
      for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
          sum += image[i + di][j + dj]
      blurred_row.append(sum // 9)
    blurred.append(blurred_row)
  return blurred