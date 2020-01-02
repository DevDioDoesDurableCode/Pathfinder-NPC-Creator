from random import randint

#Base Stats List
stats = {}

#Dice Variables
diceA = 0
diceB = 0
diceC = 0
diceD = 0

#Value Place Holder
statCreationHolder = {}
statHolder = {}
statHolderPlacement = 0
statHolderPointer = 0

#Smallest Value Searching
currSmolValue = "A"
currSmolValuePlace = 0

def baseRollStats():
  global statHolder, statHolderPlacement, statHolderPointer

  while(statHolderPlacement<=5):
    diceA = randint(1,6)
    diceB = randint(1,6)
    diceC = randint(1,6)
    diceD = randint(1,6)
    statCreationHolder[0] = diceA
    statCreationHolder[1] = diceB
    statCreationHolder[2] = diceC
    statCreationHolder[3] = diceD
    currSmolValue = "A"
    currSmolValuePlace = 0
    if(statCreationHolder [currSmolValuePlace]>diceB): 
      currSmolValue = "B"
      currSmolValuePlace = 1
    if(statCreationHolder[currSmolValuePlace]>diceC): 
      currSmolValue = "C"
      currSmolValuePlace = 2
    if(statCreationHolder[currSmolValuePlace] >diceD): 
      currSmolValue = "D"
      currSmolValuePlace = 3
    statCreationHolder[currSmolValuePlace] = 0
    statHolder[statHolderPlacement] = statCreationHolder[0]+statCreationHolder[1]+statCreationHolder[2]+statCreationHolder[3]
    statHolderPlacement += 1
  keyHole = 0
  for key, value in sorted(statHolder.iteritems(), key=lambda (k,v): (v,k)):
    statHolder[keyHole] = value
    keyHole += 1
  return statHolder

