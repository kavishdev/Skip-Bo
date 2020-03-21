import  random
maindeck = list((1,2,3,4,5,6,7,8,9,10,11,12) *12)
skipbo = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
maindeck.extend(skipbo)
random.shuffle(maindeck)      

opendeck1 = list
opendeck2 = list
opendeck3 = list
opendeck4 = list
topopen = list

def Firstcards() :
    tmp = opendeck1(0)
    topopen.insert(tmp)
    tmp = opendeck2(0)
    topopen.insert(tmp)
    tmp = opendeck3(0)
    topopen.insert(tmp)
    tmp = opendeck4(0)
    topopen.insert(tmp)

