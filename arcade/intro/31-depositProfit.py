# ---
# dateAttempted: 2024-06-21
# time: 20:11
# url: https://app.codesignal.com/arcade/intro/level-7/8PxjMSncp9ApA4DAb
# tags:
#   - arcade
# ---
def solution(deposit, rate, threshold):
  years = 0
  while deposit < threshold:
    deposit *= ((100 + rate) / 100)
    years += 1
  return years