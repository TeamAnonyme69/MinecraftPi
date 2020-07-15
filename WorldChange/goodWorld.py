
from mcpi.minecraft import Minecraft
from random import randint


mc = Minecraft.create()

x = 127
y = 64
z = 127
block = 0


for a in range(256):
  z = 127
  for b in range(256):
    y = mc.getHeight(x,z)
    y = y + 64
    for c in range(y):
      bl = mc.getBlock(x, y, z)
      if bl == 0 :
        pass
      else :
        random = randint(0, 10)
        if random == 1 :
          block = 57
        elif random == 2 :
          block = 22
        elif random == 3 :
          block = 41
        elif random == 4
          block == 42
        elif random == 5 :
          block = 21
        elif random == 6 :
          block = 14
        elif random == 7 :
          block = 15
        elif random == 8 :
          block == 16
        elif random == 9 :
          block == 56
        else :
          block = 247
        mc.setBlock(x,y,z,block)
      y = y - 1
    z = z - 1
  x = x - 1
