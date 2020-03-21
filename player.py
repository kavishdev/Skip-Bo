from lists import *
from gamerules import clear
class player ():
    message = """
    Options 0  : Pick card from maindeck
    Options 1  : Own Top of main cards
    Options 2  : card from hand,  ask index
    Options 3  : from discard pile, ask index
    Options 4  : pass, ask index from hand 
    """
    lmain = []
    lhand = []
    ldiscard = []
    name = ''
    def __init__(self,name="Uknown"):
        self.name=name

    def AskName(self):
       self.name = input("Enter the player name :")
        
    def TellName(self):
        print ("Player name :",self.name)

    def setmaincard (self,cards):
        self.lmain=cards

    def sethandcard (self,cards):
        self.lhand=cards

    def topmaincard (self):
        return self.lmain[0]
        pass
    def countofmaincard(self):
        return len(self.lmain)
        pass

    def Info(self,current=False):
        print("===== ",self.name,"===== TopCard ",self.topmaincard(),"------Hand Cards-------",self.lhand)
        print("\tDiscardCards ",self.ldiscard)

    def options(self):
        print(self.message)
        Option  = int(input(" Option 0('0' without brackets), Option1('1' without brackets) , Option 2('2' without brackets), Option 3('3' without brackets), Option 4 ('4' without brackets) ") )
        return Option
        
    def optionswithout0(self):
        print(self.message)
        inputtakenafter0  = int(input("Option1('1' without brackets) , Option 2('2' without brackets), Option 3('3' without brackets), Option 4 ('4' without brackets) ") )
 
        pass
    def play(self):
        Option = self.options()
        if Option  == 0 :
            tmp = maindeck.pop()
            self.lhand.append(tmp)
            from lists import *
            self.Info()
            self.optionswithout0()
            pass

        
        if self.options == 1 :
            tmp = list.remove(self.topmaincard())
            list.insert(0,tmp)
            self.topmaincard()
            print(self.topmaincard())
        
        if self.options == 2 :
            tmp = list.remove(self.topmaincard)
            list.insert(0,tmp)
        
        
    


