moves = []
c,r = list(map(int,input().split()))
posx = 0
posy = 0
while True:
  x,y = list(map(int,input().split()))
  if x == 0 and y == 0:
    break
  posx += x
  posy += y
  if posx > c:
    posx = c
  elif posx < 0:
    posx = 0
  if posy > r:
    posy = r
  elif posy < 0:
    posy = 0
  print(posx,posy)
