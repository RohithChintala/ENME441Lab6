import random
ay = 0
ax = 0
g = 0b1
mask = 0b11111111
for l in range(10):
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
  #g <<= ax
  #print(bin(~g & mask))
  f = g << (8-ax)
  print('a =',ax)
  e = ~f & mask
  print('e =',bin(e))
  #print(~g & mask)
  