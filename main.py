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
  if ax >= 0:
    if ax <= 7:
      if ay >= 0:
        if ay <= 7:
          h = 1
    else:
      h = 0
      ax -= x
      ay -= y
  f = g << abs(7-ax)
  e = ~f & mask
  print(e)