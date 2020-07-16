#a floor is lava game but its a parkour, not a survival


from mcpi.minecraft import Minecraft
from time import sleep
from random import randint

mc = Minecraft.create()

def walls():
  mc.setBlocks(-20, 0, -20, -20, 20 ,20, 246)
  sleep(3)
  mc.setBlocks(-20, 0, -20, 20, 20, -20, 246)
  sleep(3)
  mc.setBlocks(20, 0, 20, -20, 20, 20, 246)
  sleep(3)
  mc.setBlocks(20, 0, 20, 20, 20, -20, 246)
  sleep(3)
  mc.setBlocks(-20, -1, -20, 20, -1, 20, 246)
  sleep(3)
  
def lava(y):
  mc.setBlocks(19, y, 19, -19, y, -19, 10)
  
def wait(s): #le temps dans la cage de depart
  sa = s / 10
  sb = s*10
  for a in range(sb):
    color = randint(1, 14)
    mc.player.setPos(0, 3, 0)
    mc.setBlock(0, 2, 0, 35, color)
    sleep(sa)
