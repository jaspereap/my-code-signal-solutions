# ---
# dateAttempted: 2024-06-21
# time: 20:07
# url: https://app.codesignal.com/arcade/intro/level-8/8N7p3MqzGQg5vFJfZ
# tags:
#   - arcade
# ---
def solution(s):
  tmp = []
  for c in s:
    if c not in tmp:
      tmp.append(c)
  return len(tmp)