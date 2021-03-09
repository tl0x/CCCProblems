start = int(input())
end = int(input())
x = 0

def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return len(result)

for i in range(start,end+1):
  if factors(i) == 4:
    x += 1

print("The number of RSA numbers between " + str(start) + " and " + str(end) + " is " + str(x) + "."
)