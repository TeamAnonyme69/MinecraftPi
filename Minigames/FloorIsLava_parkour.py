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
  
def wait(): #le temps dans la cage de depart
  for c in range(5, 1): 
    for a in range(10):
      color = randint(1, 14)
      mc.player.setPos(0, 3, 0)
      mc.setBlock(0, 2, 0, 35, color)
      sleep(0.1)
    mc.postToChat(c)
def mainloop():
  walls()
  wait()
  
  
