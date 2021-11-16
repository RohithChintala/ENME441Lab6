import time
from shifter import Shifter    # extend by composition
import multiprocessing

class LED8x8Copy(multiprocessing.Process):
  def __init__(self, data, latch, clock, num, a):
    self.shifter = Shifter(data, latch, clock)
    p = multiprocessing.Process(target = self.display, args = (num, a))
    #multiprocessing.Process.__init__(self, target=self.display)
  def display(self, num, a):
    self.shifter.shiftByte(a[num])
    self.shifter.shiftByte(1 << (num))
