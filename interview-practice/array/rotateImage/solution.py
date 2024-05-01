def solution(a):
  n = len(a)
  ans = [[0]*n for i in range(n) ]
  for i in range(n):
    for j in range(n):
      ans[j][n - i - 1] = a[i][j]
  return ans