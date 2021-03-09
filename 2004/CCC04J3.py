n = int(input())
m = int(input())

adjectives = []
nouns = []
for i in range(n):
  adjectives.append(input())
for i in range(m):
  nouns.append(input())

for i in range(len(adjectives)):
  for j in range(len(nouns)):
    print(adjectives[i] + " as " + nouns[j])
