skillStore = {}
skillNames = {}
skillMod = [[0]*4 for i in range(36)]
#Acrobatics

#Appraise

#Bluff
#Climb
#Craft
Str = 0
Dex = 0
Con = 0
Int = 0
Wis = 0
Cha = 0 
def raceSkillModing(editSkill, editMod):
  for i in range(0, len(editSkill)):
    skillMod[editSkill[i]][3] += editMod[i]
  return

def skillGen(Str, Dex, Con, Int, Wis, Cha, classSkillList, skillPoints):
  global skillStore, skillNames, skillMod
  skillStore[1] = (Dex-10)/2
  skillNames[1] = "Acrobatics"
  skillMod[1][1] = (Dex-10)/2
  skillStore[2] = (Int-10)/2
  skillNames[2] = "Appraise"
  skillMod[2][1] = (Int-10)/2
  skillStore[3] = (Cha-10)/2
  skillNames[3] = "Bluff"
  skillMod[3][1] = (Cha-10)/2
  skillStore[4] = (Str-10)/2
  skillNames[4] = "Climb"
  skillMod[4][1] = (Str-10)/2
  skillStore[5] = (Cha-10)/2
  skillNames[5] = "Diplomacy"
  skillMod[5][1] =(Cha-10)/2
  skillStore[6] = (Dex-10)/2
  skillNames[6] = "Disable Device"
  skillMod[6][1] = (Dex-10)/2
  skillStore[7] = (Cha-10)/2
  skillNames[7] = "Disguise"
  skillMod[7][1] = (Cha-10)/2
  skillStore[8] = (Dex-10)/2
  skillNames[8] = "Escape Artist"
  skillMod[8][1] =(Dex-10)/2
  skillStore[9] = (Dex-10)/2
  skillNames[9] = "Fly"
  skillMod[9][1] = (Dex-10)/2
  skillStore[10] = (Cha-10)/2
  skillNames[10] = "Handle Animal"
  skillMod[10][1] = (Cha-10)/2
  skillStore[11] = (Wis-10)/2
  skillNames[11] = "Heal"
  skillMod[11][1] = (Wis-10)/2
  skillStore[12] = (Cha-10)/2
  skillNames[12] = "Intimidate"
  skillMod[12][1] = (Cha-10)/2
  skillStore[13] = (Int-10)/2
  skillNames[13] = "Knowledge(Arcana)"
  skillMod[13][1] = (Int-10)/2
  skillStore[14] = (Int-10)/2
  skillNames[14] = "Knowledge(Dungeoneering)"
  skillMod[14][1] = (Int-10)/2
  skillStore[15] = (Int-10)/2
  skillNames[15] = "Knowledge(Engineering)"
  skillMod[15][1] = (Int-10)/2
  skillStore[16] = (Int-10)/2
  skillNames[16] = "Knowledge(Geography)"
  skillMod[16][1] = (Int-10)/2
  skillStore[17] = (Int-10)/2
  skillNames[17] = "Knowledge(History)"
  skillMod[17][1] = (Int-10)/2
  skillStore[18] = (Int-10)/2
  skillNames[18] = "Knowledge(Local)"
  skillMod[18][1] = (Int-10)/2
  skillStore[19] = (Int-10)/2
  skillNames[19] = "Knowledge(Nature)"
  skillMod[19][1] = (Int-10)/2
  skillStore[20] = (Int-10)/2
  skillNames[20] = "Knowledge(Nobility)"
  skillMod[20][1] = (Int-10)/2
  skillStore[21] = (Int-10)/2
  skillNames[21] = "Knowledge(Planes)"
  skillMod[21][1] = (Int-10)/2
  skillStore[22] = (Int-10)/2
  skillNames[22] = "Knowledge(Religion)"
  skillMod[22][1] = (Int-10)/2
  skillStore[23] = (Int-10)/2
  skillNames[23] = "Linguistics"
  skillMod[23][1] = (Int-10)/2
  skillStore[24] = (Wis-10)/2
  skillNames[24] = "Perception"
  skillMod[24][1] = (Wis-10)/2
  skillStore[25] = (Cha-10)/2
  skillNames[25] = "Perform"
  skillMod[25][1] =(Wis-10)/2
  skillStore[26] = (Cha-10)/2
  skillNames[26] = "Perform"
  skillMod[26][1] = (Cha-10)/2
  skillStore[27] = (Wis-10)/2
  skillNames[27] = "Profession"
  skillMod[27][1] = (Wis-10)/2
  skillStore[28] = (Dex-10)/2
  skillNames[28] = "Ride"
  skillMod[28][1] = (Dex-10)/2
  skillStore[29] = (Wis-10)/2
  skillNames[29] = "Sense Motive"
  skillMod[29][1] = (Wis-10)/2
  skillStore[30] = (Dex-10)/2
  skillNames[30] = "Sleight of Hand"
  skillMod[30][1] = (Dex-10)/2
  skillStore[31] = (Int-10)/2
  skillNames[31] = "Spellcraft"
  skillMod[31][1] = (Int-10)/2
  skillStore[32] = (Dex-10)/2
  skillNames[32] = "Stealth"
  skillMod[32][1] = (Dex-10)/2
  skillStore[33] = (Wis-10)/2
  skillNames[33] = "Survival"
  skillMod[33][1] = (Wis-10)/2
  skillStore[34] = (Str-10)/2
  skillNames[34] = "Swim"
  skillMod[34][1] = (Str-10)/2
  skillStore[35] = (Cha-10)/2
  skillNames[35] = "Use Magic Device"
  skillMod[35][1] = (Cha-10)/2
  length = 0
  select = 0
  for i in range(1, len(skillNames)-1):
    skillMod[i][1] = skillStore[i]
  while(length<len(classSkillList)):
    select = classSkillList[length]
    skillStore[select] += 3
    skillNames[select] = "*"+skillNames[select]
    skillMod[select][0] += 3
    if(skillPoints>0):
      skillStore[select] += 1
      skillMod[select][2] += 1
      skillPoints -= 1
    length += 1
  while(skillPoints>0):
    length = 0
    while(length<len(classSkillList) and skillPoints>0):
      select = classSkillList[length]
      skillMod[select][2] += 1
      skillStore[select] += 1
      length += 1
      skillPoints -= 1
  for i in range(1, len(skillMod)):
    skillMod[i][3] += skillMod[i][0]
    skillMod[i][0] = skillMod[i][3]+skillMod[i][1]+skillMod[i][2]
  return
    

def pullSkillStore(select):
  return skillStore[select]

def pullSkillNames(select):
  return skillNames[select]

def pullSkillVals():
  return skillMod