m = int(input())
n = int(input())
x =0 

for i in range(1,m+1):
  for j in range(1,n+1):
    if i + j == 10:
      x += 1



if x == 1: 
  print('There is '+ str(x) + ' way to form the sum 10.')
else:
  print('There are '+ str(x) + ' ways to form the sum 10.')