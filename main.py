from gamerules import *
from lists import *
from player import *
from time import sleep
welcome()
 
p1 = player("K")
p2 = player("S")

# p1.AskName()
#p2.AskName()

p1.TellName()
p2.TellName()

print(maindeck)

tmp1 = []
tmp2 = []
for i in range (10):
    tmp1.append(maindeck.pop())
    tmp2.append(maindeck.pop())

p1.setmaincard(tmp1)
p2.setmaincard(tmp2)

print (maindeck)

# sleep(2)
tmp1 = []
tmp2 = []
for i in range (5):
    tmp1.append(maindeck.pop())
    tmp2.append(maindeck.pop())

p1.sethandcard(tmp1)
p2.sethandcard(tmp2)
# clear()

print( p1.name," hand card are ",p1.lhand)
# sleep(2)
# clear()
print( p2.name , " hand card are ",p2.lhand)
# sleep(2)
# clear()
print( p1.name,"'s top main card is ",p1.topmaincard())
print( p2.name , "'s top main card is ",p2.topmaincard())

print( p1.name,"'s left main card are ",p1.countofmaincard())
print( p2.name , "'s left main card are ",p2.countofmaincard())



# THIS part of the code.. will ask Step 1 : Option from each Player and The after each option, Step 2 :  Validate the Option, Step 3 : IF true EXECUTE option Step 4 : Loop if not valid step

print("---------------- DECK ------------")
print("\t \t Deck Stacks ",topopen())

p1.Info()
p2.Info()
  
p1.play()