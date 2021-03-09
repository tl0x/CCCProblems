x = int(input())
m = int(input())
a = True
for n in range(1,m):
  if (x*n) % m == 1:
    print(n)
    x = False
    break

if x == True:
  print("No such integer exists.")