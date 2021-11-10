import time
from led_display import LED8x8

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 13, 19, 26

# Pick a number sequence
sequence = [8, 6, 7, 5, 3, 0, 9]
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
    LED.display(n)
    time.sleep(0.001)