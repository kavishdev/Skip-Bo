from os import *
def welcome ():
    print ("welcome to the game of skip bo for two players")

def clear(): 
  
        _ = system('clear')
        

def play(self):
    print(self.message)
    self.options()
    if self.options  == 0 :
        tmp = list.pop(maindeck)
        list.insert(0,tmp)
    
    if self.options == 1 :
        tmp = list.remove(self.topmaincard())
        list.insert(0,tmp)
        self.topmaincard()
        print(self.topmaincard())
    
    if self.options == 2 :
        tmp = list.remove(self.topmaincard)
        list.insert(0,tmp)
    
    
    pass
