# ---
# dateAttempted: 2024-06-21
# time: 20:09
# url: https://app.codesignal.com/arcade/intro/level-7/PTWhv2oWqd6p4AHB9
# tags:
#   - arcade
# ---
# def solution(inputArray):
#   inputArray = sorted(inputArray)
#   print(inputArray)
#   for i in range(0, len(inputArray) - 1):
#     current_elem = inputArray[i]
#     next_elem = inputArray[i + 1]
#     diff_count = 0
#     print(f'current: {current_elem}, next: {next_elem}')
#     for idx, char in enumerate(current_elem):
#       print(f'char: {char}, next_elem[idx]: {next_elem[idx]}')
#       print(f'not_eq: {char != next_elem[idx]}')
#       if char != next_elem[idx]:
#         diff_count += 1
#     print(f'diff_count: {diff_count}')
#     if diff_count > 1 or diff_count < 1:
#       return False
#   return True
from itertools import permutations

def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def solution(inputArray):
    for z in permutations(inputArray):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(inputArray) - 1:
            return True
    return False