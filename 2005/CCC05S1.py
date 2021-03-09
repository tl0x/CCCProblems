n = int(input())
phonenums = []
alphaToInt = "22233344455566677778889999"
for i in range(n):
  ele = input()
  temp = ""
  for c in range(len(ele)):
    if ele[c] == '-':
      continue
    temp += ele[c]
  ele = temp
  ele = ele[0:10]
  temp1 = ele.clone()
  for c in range(len(ele)):
    if ord(ele[c]) >= 65  and ord(ele[c]) <= 90:
      temp += alphaToInt[ord(ele[c]) - ord('A')-1]

  print(ele[0:3] + "-" + ele[3:3] + "-" + ele[6:4])