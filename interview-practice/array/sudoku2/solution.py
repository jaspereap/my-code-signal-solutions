def solution(grid):
  # Check row
  uniqueDict = {}
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      # print(grid[i][j])
      if grid[i][j] != '.':        
        if grid[i][j] not in uniqueDict:
          uniqueDict[grid[i][j]] = 1
        else:
          print("Row failed")
          return False
    uniqueDict = {}
      
  # Check col
  for col in zip(*grid):
    # print(col)
    for num in col:
      if num != '.':
        if num not in uniqueDict:
          uniqueDict[num] = 1
        else:
          print('Col failed')
          return False
    uniqueDict = {}
        
  # Check grid
  for i in range(0, len(grid), 3):
    for j in range(0, len(grid), 3):
      for k in range(i, i + 3):
        for l in range(j, j + 3):
          # print(f"i:{i}, j:{j}, k:{k}, l:{l}")
          if grid[k][l] != '.':
            if grid[k][l] not in uniqueDict:
              uniqueDict[grid[k][l]] = 1
            else:
              print("Grid failed")
              return False
      uniqueDict = {}
  return True