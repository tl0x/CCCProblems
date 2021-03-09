# CCC '06 S1 - Maternity
#
# Language : Python
# Algorithm:
# Use string processing techniques and simple operators to determine if there is a possible baby
# This question confused me at first, but is actually really easy!
#

parent1 = input()
parent2 = input()
n = int(input())

def possibleBabies(m,f,b):
  lst = []
  flag = True
  for i in range(5):
    if b[i] >= 'A' and b[i] <= 'E':
      if b[i] == 'A':
        flag = ("A" in m[i*2:i*2+1]) or ('A' in f[i*2:i*2+1])
      elif b[i] == 'B':
        flag = "B" in m[i*2:i*2+1] or ('B' in f[i*2:i*2+1])
      elif b[i] == 'C':
        flag = "C" in m[i*2:i*2+1] or ('C' in f[i*2:i*2+1])
      elif b[i] == 'D':
        flag = "D" in m[i*2:i*2+1] or ('D' in f[i*2:i*2+1])
      elif b[i] == 'E':
        flag = "E" in m[i*2:i*2+1] or ('E' in f[i*2:i*2+1])
      lst.append(flag)
    else:
      if b[i] == 'a':
        flag = ("a" in m[i*2:i*2+2]) and ('a' in f[i*2:i*2+2])
      elif b[i] == 'b':
        flag = "b" in m[i*2:i*2+2] and ('b' in f[i*2:i*2+2])
      elif b[i] == 'c':
        flag = "c" in m[i*2:i*2+2] and ('c' in f[i*2:i*2+2])
      elif b[i] == 'D':
        flag = "d" in m[i*2:i*2+2] and ('d' in f[i*2:i*2+2])
      elif b[i] == 'e':
        flag = "e" in m[i*2:i*2+2] and ('e' in f[i*2:i*2+2])
      lst.append(flag)

  if False in lst:
    return False
  else:
    return True

for i in range(n):
  baby = input()
  if possibleBabies(parent1,parent2,baby) == True:
    print("Possible baby.")
  elif possibleBabies(parent1,parent2,baby) == False:
    print("Not their baby!")


