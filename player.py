from lists import *
class player ():

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
    def centerify(text, width=-1):
        lines = text.split('\n')
        width = max(map(len, lines)) if width == -1 else width
        return '\n'.join(line.center(width) for line in lines)

    def Info(self,current=False):
        print("===== ",self.name,"===== TopCard ",self.topmaincard())
        print("\tDiscardCards ",self.ldiscard)
    def options(self):
        ask =  input(" Option 0('0' without brackets), Option1('1' without brackets) , Option 2('2' without brackets), Option 3('3' without brackets), Option 4 ('4' without brackets) ")
        return ask
        pass
    
    def aske(self, parameter_list):
        pass

    message = """
    Options 0  : Pick card from miandeck
    Options 1  : Own Top of main cards
    Options 2  : card from hand,  ask index
    Options 3  : from discard pile, ask index
    Options 4  : pass, ask index from hand 
    """


