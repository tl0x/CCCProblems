a = input()
b= input()
a = a.replace(' ','')
b = b.replace(' ','')
a = sorted(a)
b = sorted(b)

if a == b:
  print("Is an anagram.")
else:
  print("Is not an anagram.")
