from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
def verifBlock(x, y, z):
    mc.setBlock(x, y, z, 35, 15)
    
def main():
    x = 85
    for a in range(254):
        z = 121
        for b in range(254):
            high = mc.getHeight(x,z)
            high = high - 1
            y = high
            bloc = mc.getBlock(x, y, z )
            verifBlock(x, y, z, bloc)
            for c in range(20):
                y = y - 1
                #Get block of x y z
                verifBlock(x, y, z)
                    
            z = z - 1
        x = x - 1

main()
