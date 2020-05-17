import math
total = 0
filepath = 'fuel.txt'
with open(filepath) as fp:
   line = fp.readline()
   for line in fp:
       x = int(line)
       total += math.floor(x / 3) - 2
print(total)
