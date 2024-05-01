def solution(s):
  hash = {}
  for c in s:
    if c not in hash.keys():
      hash[c] = 1
    else:
      hash[c] += 1
  for k, v in hash.items():
    if v == 1:
      return k
  return "_"