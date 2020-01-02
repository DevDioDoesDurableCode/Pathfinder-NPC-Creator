extraSlots = [[0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5],[0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4],[0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4],[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4],[0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4],[0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3],[0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3],[0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3],[0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3]]
spellSlotNames = [""]*10
def pullSpellSlots(level, Class,Str,Dex,Con,Int,Wis,Cha):
  global spellSlots, extraSlots, spellSlotNames
  if Class == "Bard":
    spellSlots = [0]*6
    spellSlotsTemp = [[1,2,3,3,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5],[0,0,0,1,2,3,3,4,4,4,4,5,5,5,5,5,5,5,5,5],[0,0,0,0,0,0,1,2,3,3,4,4,4,4,5,5,5,5,5,5],[0,0,0,0,0,0,0,0,0,1,2,3,3,4,4,4,4,5,5,5],[0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,3,4,4,5,5],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4,5]]
    spellSlotNames = ["1st","2nd","3rd","4th","5th","6th"]
    mod = (Cha-10)/2
    for i in range(0,6):
      spellSlots[i] = spellSlotsTemp[i][level]
      spellSlots[i] += extraSlots[i+1][mod]
  if Class == "Cleric":
    spellSlots = [0]*10
    spellSlotsTemp = [[3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4],[0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4],[0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4],[0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4],[0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4],[0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4]]
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
    mod = (Wis-10)/2
    for i in range(0,9):
      spellSlots[i] = spellSlotsTemp[i][level]
      spellSlots[i] += extraSlots[i][mod]
  if Class == "Druid":
    spellSlots = [0]*10
    spellSlotsTemp = [[3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4],[0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4],[0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4],[0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4],[0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4],[0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4]]
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
    mod = (Wis-10)/2
    for i in range(0,9):
      spellSlots[i] = spellSlotsTemp[i][level]
      spellSlots[i] += extraSlots[i][mod]
  if Class == "Paladin":
    spellSlots = [0]*4
    spellSlotsTemp = [[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4],[0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4],[0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,3]]
    spellSlotNames = ["1st","2nd","3rd","4th"]
    mod = (Cha-10)/2
    for i in range(0,4):
      spellSlots[i] = spellSlotsTemp[i][level]
      spellSlots[i] += extraSlots[i+1][mod]
  if Class == "Ranger":
    spellSlots = [0]*4
    spellSlotsTemp = [[0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4],[0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4],[0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,3]]
    spellSlotNames = ["1st","2nd","3rd","4th"]
    mod = (Wis-10)/2
    for i in range(0,4):
      spellSlots[i] = spellSlotsTemp[i][level]
      spellSlots[i] += extraSlots[i+1][mod]
  if Class == "Sorcerer":
    spellSlots = [0]*10
    spellSlotsTemp = [[3,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],[0,0,0,3,4,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6],[0,0,0,0,0,3,4,5,6,6,6,6,6,6,6,6,6,6,6,6],[0,0,0,0,0,0,0,3,4,5,6,6,6,6,6,6,6,6,6,6],[0,0,0,0,0,0,0,0,0,3,4,5,6,6,6,6,6,6,6,6],[0,0,0,0,0,0,0,0,0,0,0,3,4,5,6,6,6,6,6,6],[0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,5,6,6,6,6],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,5,6,6],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,4,6]]
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
    mod = (Cha-10)/2
    for i in range(0,9):
      spellSlots[i] = spellSlotsTemp[i][level]
      spellSlots[i] += extraSlots[i][mod]
  if Class == "Wizard":
    spellSlots = [0]*10
    spellSlotsTemp = [[3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4],[0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4],[0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4],[0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4,4,4],[0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4,4,4],[0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4,4,4],[0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,3,4,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,3,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,3,4]]
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
    mod = (Int-10)/2
    for i in range(0,9):
      spellSlots[i] = spellSlotsTemp[i][level]
      spellSlots[i] += extraSlots[i][mod]
  return spellSlots

def pullSlotNames(Class):
  if Class == "Wizard":
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
  if Class == "Sorcerer":
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
  if Class == "Ranger":
    spellSlotNames = ["1st","2nd","3rd","4th"]
  if Class == "Paladin":
    spellSlotNames = ["1st","2nd","3rd","4th"]
  if Class == "Druid":
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
  if Class == "Cleric":
    spellSlotNames = ["0 Level","1st","2nd","3rd","4th","5th","6th","7th","8th","9th"]
  if Class == "Bard":
    spellSlotNames = ["1st","2nd","3rd","4th","5th","6th"]

  return spellSlotNames