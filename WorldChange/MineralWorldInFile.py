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
def init():
    f = open("file.py","w")
    f.write("#Code by Eric42053\n")
    f.close()
    f = open("file.py","a")
    f.write("\nfrom mcpi.minecraft import Minecraft\nfrom time import sleep\n\nmc = Minecraft.create()\n")
    
def write(x, y, z, mineral):
    strmineral = ""
    if mineral == 21 :
        strmineral = "Lapis_Lazuli_Ore"
    elif mineral == 56 :
        strmineral = "Diamond_Ore"
    elif mineral == 14 :
        strmineral = "Gold_Ore"
    elif mineral == 15 :  
        strmineral = "Iron_Ore"
    elif mineral == 16 :
        strmineral = "Coal_ore"
    elif mineral == 73 :
        strmineral = "Redstone_Ore"
    f = open("file.py", "a")
    f.write("\nmc.setBlock(" + str(x) + "," + str(y) + "," + str(z) + "," + str(mineral) + ") # " + str(strmineral))
    f.close()
    
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
    init()
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
                    write(x, y, z, bl)
                else :
                    stoneOrOthers = stoneOrOthers + 1
                y = y - 1
            count = count + 1
            actualize(x, z, mined, minerals, count, coal, lapis, diamond, iron, redstone, gold)
            z = z - 1
        x = x - 1
    

main()
