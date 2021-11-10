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

#theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)
LED= LED8x8(dataPin, latchPin, clockPin)
ay = 0
ax = 0
while True:
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
` g <<= ax 
  a = multiprocessing.Array('i',8)
  a[ay] = g
  p = multiprocessing.Process(name='myname',target=LED.display(ay, a),args=(ay, a))
  p.daemon = True
  p.start()
  time.sleep(0.1)
