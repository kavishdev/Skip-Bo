import  random
maindeck = []
for sets in range (12):  
    for numb in range (12):
        maindeck.append(numb + 1) 

for numb in range (18):
        maindeck.append("*") 
             
random.shuffle(maindeck)      

opendeck1 = []
opendeck2 = []
opendeck3 = []
opendeck4 = []
topopen = []

def topopen():
    tmp=[]
    if len(opendeck1)==0: 
        tmp.append("X")
    else:
        tmp.append(len(opendeck1))

    if len(opendeck2)==0: 
        tmp.append("X")
    else:
        tmp.append(len(opendeck2))
    if len(opendeck3)==0: 
        tmp.append("X")
    else:
        tmp.append(len(opendeck3))

    if len(opendeck4)==0: 
        tmp.append("X")
    else:
        tmp.append(len(opendeck4))
    
    return tmp

