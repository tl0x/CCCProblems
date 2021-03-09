pos = 1

while True:
  roll = int(input())
  if roll == 0:
    print("You Quit!")
    break
  if pos + roll<= 100:
    pos += roll
  if pos == 9:
    pos = 34
  if pos == 40:
    pos = 64
  if pos == 67:
    pos = 86
  if pos == 54:
    pos = 19
  if pos == 90:
    pos = 48
  if pos == 99:
    pos = 77
  print("You are now on square",pos)
  if pos == 100:
    print("You Win!")
    break