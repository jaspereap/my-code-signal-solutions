# ---
# dateAttempted: 2024-06-21
# time: 19:58
# url: https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo
# tags:
#   - array
#   - arcade
# ---
def solution(bishop, pawn):
  bishopCoord = toCoord(bishop)
  pawnCoord = toCoord(pawn)
  y_diff = abs(bishopCoord[0] - pawnCoord[0])
  x_diff = abs(bishopCoord[1] - pawnCoord[1])
  if y_diff - x_diff == 0:
    return True
  return False

def toCoord(s):
  return (8 - int(s[1]), ord(s[0]) - 97)