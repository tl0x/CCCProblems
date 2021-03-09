vowel=['a', 'e', 'i', 'o', 'u', 'y']
consonant=['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
going = True
while going:
  ele = input()
  if ele == "quit!":
    break
  if len(ele) > 4:
    if ele[-3] in consonant:
      if ele[-2] == vowel[3]:
        if ele[-1] == consonant[13]:
          for i in range(len(ele)-2):
            print(ele[i], end = "")
          print("our")
        else:
          print(ele)
      else:
        print(ele)
    else:
      print(ele)
  else:
    print(ele)