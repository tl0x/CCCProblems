n = int(input())

suitcases = [100,500,1000,5000,10000,25000,50000,100000,500000,1000000]

eliminatedsuitcases = []
for i in range(n):
  eliminatedsuitcases.append(int(input())-1)
deal = int(input())
x = 0

for i in range(10):
  if i in eliminatedsuitcases:
    continue
  else:
    x += suitcases[i]

x /= len(suitcases) - len(eliminatedsuitcases)

if float(deal) > x:
  print("deal")
elif float(deal) < x:
  print("no deal")