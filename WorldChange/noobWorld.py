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
          block = 3
        elif random == 2 :
          block = 4
        elif random == 3 :
          block = 5
        elif random == 4
          block == 12
        elif random == 5 :
          block = 13
        elif random == 6 :
          block = 46
        elif random == 7 :
          block = 24
        elif random == 8 :
          block == 30
        elif random == 9 :
          block == 3
        else :
          block = 3
        mc.setBlock(x,y,z,block)
      y = y - 1
    z = z - 1
  x = x - 1
