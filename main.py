import random
ay = 0
ax = 0

x = random.randint(-1, 1)
y = random.randint(-1, 1)
ax += x
ay += y
if ay < 0:
  ay = 7
if ay > 7:
  ay = 0
if ax < 0:
  ax = 7
if ax > 7:
  ax = 0
g = 1
g <<= ax
print(bin(g)) 