
from mcpi.minecraft import Minecraft

mc = Minecraft.create()

x = 127
y = 64
z = 127

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
        mc.setBlock(x,y,z,5)
      y = y - 1
    z = z - 1
  x = x - 1
