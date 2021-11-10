import time
from led_display import LED8x8
import multiprocessing

dataPin, latchPin, clockPin = 13, 19, 26

pattern = [ 
  0b00111100, 
  0b01000010,
  0b10100101,
  0b10000001,
  0b10100101,
  0b10011001,
  0b01000010,
  0b00111100] 

#theLEDdisplay= LEDdisplay(dataPin, latchPin, clockPin)
LED= LED8x8(dataPin, latchPin, clockPin)
while True:
  for n in range(8):
    a = multiprocessing.Array('i',8)
    a[n] = pattern[n]
    p = multiprocessing.Process(name='myname',target=LED.display(n, a),args=(n, a))
    p.daemon = True
    p.start()
    time.sleep(0.001)