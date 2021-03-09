line = input()
c1 = input()
c2 = input()
value = ""

letters = {'A': None, 'B': None, 'C': None, 'D':None, 'E': None, 'F': None, 'G': None, 'H': None, 'I':None, 'J':None, 'K':None, 'L':None, 'M':None, 'N':None, 'O':None, 'P':None, 'Q':None, 'R':None, 'S':None, 'T':None, 'U':None, 'V':None, 'W':None, 'X':None, 'Y':None, 'Z':None, ' ':None}


for i in range(len(line)):
  letters[c1[i]] = line[i]

for i in range(len(c2)):
  if c2[i] in c1:
    value += letters[c2[i]]
  else:
    value += "."

print(value)