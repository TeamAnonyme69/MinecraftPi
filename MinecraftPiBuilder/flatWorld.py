from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

mc.setBlocks(-127, 0, -127, 127, 64, 127, 0)
sleep(10)
mc.setBlocks(-127, 0, -127, 127, 0, 127, 2)
sleep(3)
mc.setBlocks(-127, -1, -127, 127, -63, 127, 3)
sleep(10)
