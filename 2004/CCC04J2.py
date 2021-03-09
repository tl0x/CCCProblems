start = int(input())
end = int(input())

print("All positions change in year " + str(start))

timer = start

while timer + 60 <= end:
  timer += 60
  print("All positions change in year " + str(timer))