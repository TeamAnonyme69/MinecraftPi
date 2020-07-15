from mcpi.minecrft import Minecraft
from time import sleep

mc = Minecraft.create()

#CREATE A MOB TOWER : LEVEL 1

mc.setBlocks(-20, 0,-20, 20, 0, 20,0)
sleep(2)

mc.setBlocks(-5, 0,-5,-5 30 , 5, 4)
mc.setBlocks(5, 0,-5,-5 30 , 5, 4)
mc.setBlocks(5, 0,-5,-5 30 , -5, 4)
mc.setBlocks(-5, 0,5,-5 30 , 5, 4)

