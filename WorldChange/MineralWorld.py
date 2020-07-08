print("You can only execute this program on Raspberry pi 2 , 3 , 4.")




from mcpi.minecraft import Minecraft
from time import sleep
import os

print("Program by Eric GRAVES")
print("Copyright 2020")
print("----------- WARNING ----------")
print("This program run a few moments. you need a very good computer.")
mc = Minecraft.create()
def actualize(x, z, mined, minerals, count, coal, lapis, diams, iron, redstone, gold):
    os.system("clear")
    print("Position : X : " + str(x) + " Z : " + str(z))
    print(str(mined) + " Blocks mined")
    print("or " + str(minerals) + " ores found")
    print("Coal : " + str(coal) + "\nLapis : " + str(lapis) + "\nDiamond : " + str(diams) + "\nIron : " + str(iron) + "\nRedstone : " + str(redstone) + "\nGold : " + str(gold) ) 
    
    print(str(count) + " / 64516")
def main(): 
    x = 127 #Default is 127
    y = 60
    z = 127 #Default is 127
    coal = 0
    lapis = 0
    diamond = 0
    iron = 0
    redstone = 0
    gold = 0
    minerals = 0
    mined = 0
    stoneOrOthers = 0
    count = 0
    block = [21, 56, 14, 15, 16, 73]
    for a in range(254):
        z = 127
        for b in range(254):
            y = mc.getHeight(x,z)
            ypos = y + 65
            for c in range(ypos):
                bl = mc.getBlock(x, y, z)
                mined = mined + 1
                if bl == 21 or bl == 56 or bl == 14 or bl == 15 or bl == 16 or bl == 73 :
                    
                    minerals = minerals + 1
                    if bl == 21 :
                        lapis = lapis + 1
                    elif bl == 56 :
                        diamond = diamond + 1
                    elif bl == 14 :
                        gold = gold + 1
                    elif bl == 15 :
                        iron = iron + 1
                    elif bl == 16 :
                        coal = coal + 1
                    elif bl == 73 :
                        redstone = redstone + 1
                else :
                    mc.setBlock(x, y, z, 0)
                    stoneOrOthers = stoneOrOthers + 1
                y = y - 1
            count = count + 1
            actualize(x, z, mined, minerals, count, coal, lapis, diamond, iron, redstone, gold)
            z = z - 1
        x = x - 1
    print(str(mined) + " Blocks mined")
    print(str(stoneOrOthers) + " stone or other blocks")
    print(str(minerals) + " Minerals Found.")
    print(str(diamond) + " Diamonds")
    print(str(lapis) + " Lapis Lazuli")
    print(str(gold) + " Gold")
    print(str(iron) + " Iron")
    print(str(coal) + " Coal")
    print(str(redstone) + " Redstone")
    

main()
