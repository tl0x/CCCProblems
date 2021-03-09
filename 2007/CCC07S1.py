from datetime import date
from datetime import datetime

n = int(input())

def inputbirth():
    data = input().split(' ')
    return date(int(data[0]), int(data[1]), int(data[2]))


def calculate_age():
    born = inputbirth()
    today = datetime(2007,2,27)
    extra_year = 1 if ((today.month, today.day) < (born.month, born.day)) else 0
    return today.year - born.year - extra_year

for i in range(n):
  x = calculate_age()
  if x >= 18:
    print("Yes")
  else:
    print("No")