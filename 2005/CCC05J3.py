# Weird varible only used twice (I think its useless)
stop = False
# stores the directions input
dirlist = []
#stores the locations
locations = []

#simple input
while stop == False:
  dir = input()
  place = input()
  if place == "SCHOOL":
    dirlist.append(dir)
    break
  else:
    locations.append(place)
    dirlist.append(dir)

#reverse the locations, and add home.
locations = locations[::-1]
locations.append('HOME')
dirlist = dirlist[::-1]

# Simple conditions
for i in range(len(dirlist)-1):
  if dirlist[i] == 'L':
    print("Turn RIGHT onto " + locations[i] + " street.")
  elif dirlist[i] == 'R':
    print("Turn LEFT onto " + locations[i] + " street.")

if dirlist[-1] == 'L':
  print("Turn RIGHT into your " + locations[-1] + ".")
elif dirlist[-1] == 'R':
  print("Turn LEFT into your " + locations[-1] + ".")

