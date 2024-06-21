# ---
# dateAttempted: 2024-06-09
# time: 16:38
# url: https://app.codesignal.com/arcade/intro/level-6/t97bpjfrMDZH8GJhi
# tags:
#   - arcade
#   - array
# ---
def solution(cell1, cell2):
  cell1_coor = getCoord(cell1)
  cell2_coor = getCoord(cell2)
  
  if getColor(cell1_coor) == getColor(cell2_coor):
    return True
  return False
  
def getCoord(cell):
  col = ord(cell[0]) - 65
  return [8 - int(cell[1]), col]

def getColor(coor):
  if (coor[0] % 2 == 0 and coor[1] % 2 == 0) or (coor[0] % 2 != 0 and coor[1] % 2 != 0):
    return False
  return True