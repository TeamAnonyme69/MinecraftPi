from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()
def verifBlock(x, y, z, bloc):
    if bloc == 0 :
        pass
    elif bloc == 35 :
        pass
    elif bloc == 5 or bloc == 17 :
        mc.setBlock(x, y, z, 35, 1)
    elif bloc == 8 or bloc == 22 or bloc == 9:
        mc.setBlock(x, y, z, 35, 11)
    elif bloc == 18 :
        mc.setBlock(x, y, z, 35, 5)
    elif bloc == 12 :
        mc.setBlock(x, y, z, 35, 4)
    elif bloc == 79 :
        mc.setBlock(x, y, z, 35, 3)
    elif bloc == 2 :
        mc.setBlock(x, y, z, 35, 13)
    elif bloc == 3 :
        mc.setBlock(x, y, z, 35, 12)
    elif bloc == 1 or bloc == 13:
        mc.setBlock(x, y, z, 35, 7)
    else :
        mc.setBlock(x, y, z, 35, 14)
    
def main():
    x = 66
    for a in range(254):
        z = 127
        for b in range(254):
            high = mc.getHeight(x,z)
            high = high - 1
            y = high
            bloc = mc.getBlock(x, y, z )
            verifBlock(x, y, z, bloc)
            for c in range(10):
                y = y - 1
                #Get block of x y z
                bloc = mc.getBlock(x, y, z )
                verifBlock(x, y, z, bloc)
                    
            z = z - 1
        x = x - 1

main()
