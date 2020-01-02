#Stuffs
BAB = 0
Fort = 0
Will = 0
Ref = 0
def babgenerate(classNumb, level):
  global BAB, Fort, Will, Ref
  if (classNumb == 0):
    BAB = level
    Fort = 2+(int(.5*float(level)))
    Will = (int(.34*float(level)))
    Ref = (int(.34*float(level)))
  if (classNumb == 1):
    BAB = (int(.75*float(level)))
    Fort = (int(.34*float(level)))
    Will = 2+(int(.5*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 2):
    BAB = (int(.75*float(level)))
    Fort = 2+(int(.5*float(level)))
    Will = (int(.34*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 3):
    BAB = (int(.75*float(level)))
    Fort = 2+(int(.5*float(level)))
    Will = (int(.34*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 4):
    BAB = level
    Fort = 2+(int(.5*float(level)))
    Will = (int(.34*float(level)))
    Ref = (int(.34*float(level)))
  if (classNumb == 5):
    BAB = (int(.75*float(level)))
    Fort = 2+(int(.5*float(level)))
    Will = 2+(int(.5*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 6):
    BAB = level
    Fort = 2+(int(.5*float(level)))
    Will = (int(.34*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 7):
    BAB = (int(.75*float(level)))
    Fort = (int(.34*float(level)))
    Will = 2+(int(.5*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 8):
    BAB = (int(.75*float(level)))
    Fort = (int(.34*float(level)))
    Will = 2+(int(.5*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 9):
    BAB = (int(.75*float(level)))
    Fort = (int(.34*float(level)))
    Will = 2+(int(.5*float(level)))
    Ref = 2+(int(.5*float(level)))
  if (classNumb == 10):
    BAB = (int(.75*float(level)))
    Fort = (int(.34*float(level)))
    Will = 2+(int(.5*float(level)))
    Ref = 2+(int(.5*float(level)))
  return

def pullBAB():
  global BAB
  return BAB
def pullFort():
  global Fort
  return Fort
def pullWill():
  global Will
  return Will
def pullRef():
  global Ref
  return Ref