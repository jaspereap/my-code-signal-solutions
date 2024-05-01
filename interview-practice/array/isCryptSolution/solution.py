def solution(crypt, solution):
  # print(crypt, solution)
  sol_dict = {}
  for x, y in solution:
    sol_dict[x] = y
  
  crypt_digit = []
  for i in range(len(crypt)):
    value = ""
    for letter in crypt[i]:
      value += sol_dict[letter]
    if len(value) != 1 and value[0] == '0':
      return False
    crypt_digit.append(value)

  if int(crypt_digit[0]) + int(crypt_digit[1]) == int(crypt_digit[2]):
    return True
  else:
    return False