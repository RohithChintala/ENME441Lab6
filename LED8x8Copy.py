import time
from shifter import Shifter    # extend by composition
import multiprocessing

class LED8x8Copy(multiprocessing.Process):
  def __init__(self, data, latch, clock, num, a, process_name):
    self.shifter = Shifter(data, latch, clock)
    multiprocessing.Process.__init__(self, name=process_name)
  def display(self, num, a):
    self.shifter.shiftByte(a[num])
    self.shifter.shiftByte(1 << (num))