from random import randint
armor = [[""],[""]]
def weaponGrab():
  global AC, armor
  i = randint(0, len(armor))
  y = randint(0, len(armor[i]))
  arm = armor[i][y]
  return arm