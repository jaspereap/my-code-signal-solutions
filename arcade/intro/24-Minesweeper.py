# ---
# dateAttempted: 2024-06-09
# time: 14:07
# url: https://app.codesignal.com/arcade/intro/level-5/ZMR5n7vJbexnLrgaM
# tags:
#   - "#array"
#   - arcade
# ---
def solution(matrix):
  rows = len(matrix)
  cols = len(matrix[0])
  
  ans = [ [] for i in range(rows)]

  for row in range(rows):
    for col in range(cols):
      mine_count = 0
      
      # Loop through 3x3 grid centered on matrix[row][col]
      for di in [-1,0,1]:
        for dj in [-1,0,1]:
          # Skip cell itself
          if di == 0 and dj == 0:
            continue
          # Resolve coordinates
          x = col + di
          y = row + dj
          # Check boundaries
          if x >= 0 and y >= 0 and x < cols and y < rows:
            # Increment when condition is met
            if matrix[y][x] == True:
              mine_count += 1
      ans[row].append(mine_count)
  return ans