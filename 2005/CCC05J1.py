daytime = int(input())
evening = int(input())
weekend = int(input())

A = (daytime-100)*0.25
B = (daytime-250)*0.45

if A < 0:
  A = 0

if B < 0:
  B = 0

a = round(A + (0.15*evening) + (0.2*weekend),2)
b = round(B + (0.35*evening) + (0.25*weekend),2)


print("Plan A costs " + str(a))
print("Plan B costs " + str(b))

if a == b:
  print("Plan A and B are the same price.")
elif a < b:
  print("Plan A is cheapest.")
elif a > b:
  print("Plan B is cheapest.")