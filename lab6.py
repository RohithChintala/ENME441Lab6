import time
from led_display import LED8x8
import multiprocessing
import random



dataPin, latchPin, clockPin = 13, 19, 26

pattern = [ 
  0b10000000, #0 are on
  0b01000000,
  0b00100000,
  0b00010000,
  0b00001000,
  0b00000100,
  0b00000010,
  0b00000001] 

LED= LED8x8(dataPin, latchPin, clockPin)
ay = 5
ax = 5
g = 0b1
mask = 0b11111111

while True:
  h = 0
  while h == 0:
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
  f = g << abs(8-ax)
  e = ~f & mask
  a = multiprocessing.Array('i',8) #maybe instead of i have s
  #a = multiprocessing.value('s')
  a[ay] = e
  p = multiprocessing.Process(name='myname',target=LED.display(ay, a),args=(ay, a))
  p.daemon = True
  p.start()
  time.sleep(0.1)
