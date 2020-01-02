import spellslots
import baseStats
import skills
import BABB
import weapons
import bonusClassStuffs
from random import randint

#Random Detals
align = ""
Name = ""
Gender = ""
Age = 0
Size = ""
Height = [0,0]

#Base stats
HP = 0
stats = {}
Str = 0
Dex = 0
Con = 0
Int = 0
Wis = 0
Cha = 0

#Character Factors
CR = 0
Class = ""
Race = ""

#Armor Class
AC = 0
tAC = 0
fAC = 0

#Saves
fort = 0
ref = 0
will = 0

#Attack Stats
BAB = 0
CMB = 0
CMD = 0

#Lists o' things
feats = {}
attacks = {}
specialAbility = {}

#Speedy Speed Boy
speedGround = 0
speedClimb = 0

#SystemVaribles
passCheckA = False
freeStatPoints = 0
classNumb = 0
ageAddRoll = [[0],[0],[0]]
ageRollBase = [[0],[0],[0]]
ageMarker = 0
raceSkillId = {}
raceSkillMod = {}

#Skill stuff
skillPoints = 0


#Level Selection
CR = int(input("What level do you want? "))

#Gender Generation
tempGender = ["Female","Male"]
Gender = tempGender[randint(0,1)]

#Race Selection
ask = raw_input("What race do you want? ")

if(ask == "elf" or ask == "Elf"):
  Race = "Elf"
  Size = "Medium"
  speedGround = 30
  Con -= 2
  Dex += 2
  Int += 2
  stats = baseStats.baseRollStats()
  if Gender == "Female":
    tempName = ["Amrunelara", "Dardlara", "Faunra","Jathal","Merisiel", "Oparal", "Soumral", "Tessara", "Yalandlara"]
    Name = tempName[randint(0,len(tempName)-1)]
  if Gender == "Male":
    tempName = ["Caladrel", "Heldalel", "Lanliss","Meirdrarel","Seldlon", "Talathel", "Variel", "Zordlon"]
    Name = tempName[randint(0,len(tempName)-1)]
  Age = 110
  ageAddRoll = [[4],[6],[10]]
  ageRollBase = [[6],[6],[6]]
  specialAbility[0] = "Low-Light Vision"
  specialAbility[1] = "Elven Immunities"
  specialAbility[2] = "Elven Magic"
  specialAbility[3] = "Keen Senses"
  raceSkillId[0] = 24
  raceSkillMod[0] = 2
  raceSkillId[1] = 31
  raceSkillMod[1] = 2
  skills.raceSkillModing(raceSkillId,raceSkillMod)
if(ask == "gnome" or ask == "Gnome"):
  Race = "Gnome"
  Size = "Small"
  speedGround = 20
  AC += 1
  Con += 2
  Cha += 2
  Str -= 2
  stats = baseStats.baseRollStats()
  if Gender == "Female":
    tempName = ["Besh", "Fijit", "Lini", "Neji","Majet", "Pai", "Queck", "Trig"]
    Name = tempName[randint(0,len(tempName)-1)]
  if Gender == "Male":
    tempName = ["Abroshtor", "Bastargre", "Halungalom","Krolmnite", "Poshment", "Zarzuket", "Zatqualmie"]
    Name = tempName[randint(0,len(tempName)-1)]
  Age = 40
  ageAddRoll = [[4],[6],[9]]
  ageRollBase = [[6],[6],[6]]
  specialAbility[0] = "Low-Light Vision"
  specialAbility[1] = "Defensive Training"
  specialAbility[2] = "Gnome Magic"
  specialAbility[3] = "Illusion Resistance"
  raceSkillId[0] = 24
  raceSkillMod[0] = 2
  raceSkillId[1] = 27
  raceSkillMod[1] = 2
  skills.raceSkillModing(raceSkillId,raceSkillMod)
if(ask == "human" or ask == "Human"):
  Race = "Human"
  Size = "Medium"
  speedGround = 30
  randomed = randint(1,6)
  if randomed == 1:
    Str += 2
  if randomed == 2:
    Dex += 2
  if randomed == 3:
    Con += 2
  if randomed == 4:
    Int += 2
  if randomed == 5:
    Wis += 2
  if randomed == 6:
    Cha += 2
  stats = baseStats.baseRollStats()
  if Gender == "Female":
    tempName = ["Joan","Emilia","Elizabeth","Catherine","Christina","Cait","Mia","Jessie","Victoria"]
    Name = tempName[randint(0,len(tempName)-1)]
  if Gender == "Male":
    tempName = ["Johnathan","Jospeh","George","Willam","Zach","Angus McFife XIII","Ethan","Todd","Howard","John","Kaladin"]
    Name = tempName[randint(0,len(tempName)-1)]
  Age = 15
  ageAddRoll = [[1],[1],[2]]
  ageRollBase = [[4],[6],[6]]
  specialAbility[0] = "Skilled"
if(ask == "half orc" or ask == "Half Orc"):
  Race = "Half Orc"
  Size = "Medium"
  speedGround = 30
  randomed = randint(1,6)
  if randomed == 1:
    Str += 2
  if randomed == 2:
    Dex += 2
  if randomed == 3:
    Con += 2
  if randomed == 4:
    Int += 2
  if randomed == 5:
    Wis += 2
  if randomed == 6:
    Cha += 2
  stats = baseStats.baseRollStats()
  if Gender == "Female":
    tempName = ["Canan", "Drogheda","Goruza", "Mazon","Shirish", "Tevaga", "Zeljka"]
    Name = tempName[randint(0,len(tempName)-1)]
  if Gender == "Male":
    tempName = ["Ausk", "Davor", "Hakak","Kizziar", "Makoa","Nesteruk", "Tsadok"]
    Name = tempName[randint(0,len(tempName)-1)]
  Age = 14
  ageAddRoll = [[1],[1],[2]]
  ageRollBase = [[4],[6],[6]]
  specialAbility[0] = "Darkvision"
  specialAbility[1] = "Orc Blood"
  specialAbility[2] = "Orc Ferocity"
  raceSkillId[0] = 12
  raceSkillMod[0] = 2
  skills.raceSkillModing(raceSkillId,raceSkillMod)
if(ask == "half elf" or ask == "Half Elf"):
  Race = "Half Elf"
  Size = "Medium"
  speedGround = 30
  randomed = randint(1,6)
  if randomed == 1:
    Str += 2
  if randomed == 2:
    Dex += 2
  if randomed == 3:
    Con += 2
  if randomed == 4:
    Int += 2
  if randomed == 5:
    Wis += 2
  if randomed == 6:
    Cha += 2
  stats = baseStats.baseRollStats()
  if Gender == "Female":
    tempName = ["Cathran", "Elsbeth", "Iandoli", "Kieyanna","Lialda", "Maddela", "Reda", "Tamarie"]
    Name = tempName[randint(0,len(tempName)-1)]
  if Gender == "Male":
    tempName = ["Calathes", "Encinal", "Kyras", "Narciso", "Quiray","Satinder", "Seltyiel", "Zirul"]
    Name = tempName[randint(0,len(tempName)-1)]
  Age = 20
  ageAddRoll = [[1],[2],[3]]
  ageRollBase = [[6],[6],[6]]
  specialAbility[0] = "Low-Light Vision"
  specialAbility[1] = "Elf Blood"
  specialAbility[2] = "Elven Immunities"
  specialAbility[3] = "Multitalented"
  raceSkillId[0] = 24
  raceSkillMod[0] = 2
  skills.raceSkillModing(raceSkillId,raceSkillMod)
if(ask == "halfling" or ask == "Halfling"):
  Race = "Halfling"
  Size = "Small"
  speedGround = 20
  AC += 1
  Dex += 2
  Cha += 2
  Str -= 2
  stats = baseStats.baseRollStats()
  if Gender == "Female":
    tempName = ["Anafa", "Bellis", "Etune", "Filiu", "Lissa", "Marra","Rillka", "Sistra", "Yamyra"]
    Name = tempName[randint(0,len(tempName)-1)]
  if Gender == "Male":
    tempName = ["Antal", "Boram", "Evan", "Jamir", "Kaleb", "Lem","Miro", "Sumak"]
    Name = tempName[randint(0,len(tempName)-1)]
  Age = 20
  ageAddRoll = [[2],[3],[4]]
  ageRollBase = [[4],[6],[6]]
  specialAbility[0] = "Fearless"
  specialAbility[1] = "Halfling Luck"
  raceSkillId[0] = 24
  raceSkillMod[0] = 2
  raceSkillId[1] = 1
  raceSkillMod[1] = 2
  raceSkillId[2] = 4
  raceSkillMod[2] = 2
  skills.raceSkillModing(raceSkillId,raceSkillMod)
if(ask == "dwarf" or ask == "Dwarf"):
  Race = "Dwarf"
  Size = "Small"
  speedGround = 20
  AC += 1
  Con += 2
  Wis += 2
  Cha -= 2
  stats = baseStats.baseRollStats()
  if Gender == "Female":
    tempName = ["Agna", "Bodill", "Ingra", "Kotri","Rusilka", "Yangrit"]
    Name = tempName[randint(0,len(tempName)-1)]
  if Gender == "Male":
    tempName = ["Dolgrin", "Grunyar", "Harsk", "Kazmuk","Morgrym", "Rogar"]
    Name = tempName[randint(0,len(tempName)-1)]
  Age = 40
  ageAddRoll = [[3],[5],[7]]
  ageRollBase = [[6],[6],[6]]
  specialAbility[0] = "Darkvision"
  specialAbility[1] = "Defensive Training"
  specialAbility[2] = "Greed"
  specialAbility[3] = "Stability"
  specialAbility[4] = "Stonecutting"
  

#Class Selection
ask = raw_input("What class do you want? ")

if(ask == "barbarian" or ask == "Barbarian"):
  Class = "Barbarian"
  classNumb = 0
  Str += stats[5] 
  Dex += stats[3]
  Con += stats[4]
  Int += stats[0]
  Wis += stats[2]
  Cha += stats[1]
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [1,4,10,12,19,24,28,31,32], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral"]]
  align = alignSelect[1][randint(0,1)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 0
  HP = CR*12
if(ask == "bard" or ask == "Bard"):
  Class = "Bard"
  classNumb = 1
  Str += stats[0] 
  Dex += stats[4]
  Con += stats[3]
  Int += stats[1]
  Wis += stats[2]
  Cha += stats[5]
  skillPoints = CR*(6+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [1,2,3,4,5,7,8,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,35], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  align = alignSelect[1][randint(0,2)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 1
  HP = CR*8
if(ask == "cleric" or ask == "Cleric"):
  Class = "Cleric"
  classNumb = 2
  Str += stats[3] 
  Dex += stats[2]
  Con += stats[0]
  Int += stats[1]
  Wis += stats[5]
  Cha += stats[4]
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [2,5,11,13,17,20,21,22,23,27,29,31], skillPoints)
  box = bonusClassStuffs.classExtras(Class, CR)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  if box[3] == "0":
    align = box[2]+" "+alignSelect[0][randint(0,2)]
  if box[3] == "1":
    align = alignSelect[1][randint(0,2)]+" "+box[2]

  ageMarker = 2
  HP = CR*8
if(ask == "druid" or ask == "Druid"):
  Class = "Druid"
  classNumb = 3
  Str += stats[2] 
  Dex += stats[4]
  Con += stats[3]
  Int += stats[1]
  Wis += stats[5]
  Cha += stats[0]
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [4,9,10,11,16,19,24,27,28,31,33,34], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  align = alignSelect[1][randint(0,2)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 2
  HP = CR*8
if(ask == "fighter" or ask == "Fighter"):
  Class = "Fighter"
  classNumb = 4
  Str += stats[5] 
  Dex += stats[3]
  Con += stats[4]
  Int += stats[1]
  Wis += stats[0]
  Cha += stats[2]
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [4,10,12,14,15,27,28,33,34], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  align = alignSelect[1][randint(0,2)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 1
  HP = CR*10
if(ask == "monk" or ask == "Monk"):
  Class = "Monk"
  classNumb = 5
  Str += stats[4] 
  Dex += stats[3]
  Con += stats[2]
  Int += stats[1]
  Wis += stats[5]
  Cha += stats[0]
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [1,4,8,12,17,22,24,25,26,27,28,29,32,34], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  align = "Lawful"+" "+alignSelect[0][randint(0,2)]
  ageMarker = 2
  HP = CR*8
if(ask == "paladin" or ask == "Paladin"):
  Class = "Paladin"
  classNumb = 6
  Str += stats[5] 
  Dex += stats[1]
  Con += stats[3]
  Int += stats[0]
  Wis += stats[2]
  Cha += stats[4]
  skillPoints = CR*(2+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [5,10,11,20,22,27,28,29,31], skillPoints)
  align = "Lawful Good"
  ageMarker = 1
  HP = CR*10
if(ask == "ranger" or ask == "Ranger"):
  Class = "Ranger"
  classNumb = 7
  Str += stats[4] 
  Dex += stats[5]
  Con += stats[1]
  Int += stats[2]
  Wis += stats[3]
  Cha += stats[0]
  skillPoints = CR*(6+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [4,10,11,12,14,16,19,24,27,28,31,32,33,34], skillPoints)
  box = bonusClassStuffs.classExtras(Class, CR)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  align = alignSelect[1][randint(0,2)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 1
  HP = CR*10
if(ask == "rouge" or ask == "Rouge"):
  Class = "Rouge"
  classNumb = 8
  Str += stats[1] 
  Dex += stats[5]
  Con += stats[4]
  Int += stats[0]
  Wis += stats[3]
  Cha += stats[2]
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [1,2,3,4,5,6,7,8,12,14,18,23,24,26,27,29,30,32,34,35], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  align = alignSelect[1][randint(0,2)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 0
  HP = CR*8
if(ask == "sorcerer" or ask == "Sorcerer"):
  Class = "Sorcerer"
  classNumb = 9
  Str += stats[0] 
  Dex += stats[4]
  Con += stats[3]
  Int += stats[1]
  Wis += stats[2]
  Cha += stats[5]
  box = bonusClassStuffs.classExtras(Class, CR)
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [box[1],2,3,9,12,13,27,31,35], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  align = alignSelect[1][randint(0,2)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 0
  HP = CR*6
if(ask == "wizard" or ask == "Wizard"):
  Class = "Wizard"
  classNumb = 10
  Str += stats[0] 
  Dex += stats[4]
  Con += stats[3]
  Int += stats[5]
  Wis += stats[2]
  Cha += stats[1]
  skillPoints = CR*(4+((Int-10)/2))
  skills.skillGen(Str, Dex, Con, Int, Wis, Cha, [2,9,13,14,15,16,17,18,19,20,21,22,23,24,31], skillPoints)
  alignSelect = [["Good","Neutral","Evil"],["Choatic","Neutral","Lawful"]]
  box = bonusClassStuffs.classExtras(Class, CR)
  align = alignSelect[1][randint(0,2)]+" "+alignSelect[0][randint(0,2)]
  ageMarker = 2
  HP = CR*6

for i in range(0, ageAddRoll[ageMarker][0]):
    Age = Age+randint(0, ageRollBase[ageMarker][0])

BABB.babgenerate(classNumb, CR)

#Output
print(""" """)
print(""" """)
print("Level: "+str(CR))
print("Race: "+Race)
print("Class: "+Class)
print("Gender: "+Gender)
print("Name: "+Name)
print("Age: "+str(Age))
print("Size: "+Size)
print("Speed: "+str(speedGround)+"ft")
print("Alignment: "+str(align))
if Class == "Cleric":
  print("God: "+box[0])
  print("Domain: "+box[1])
if Class == "Sorcerer":
  print("Bloodline: "+box[0])
if Class == "Wizard":
  print("School: "+box[0])
  print("Opposition schools: "+box[1])
  if box[3] == 0:
    print("Bonded Object: "+box[2])
  if box[3] == 1:
    print("Familiar: "+box[2])
if Class == "Ranger":
  if box[1] == False:
    print("Favored Enemy: "+box[0])
  if box[1] == True:
    print("Favored Enemies: "+box[0])
  if box[2] is not "1":
    if box[3] == False:
      print("Favored Terrain: "+box[2])
    if box[3] == True:
      print("Favored Terrains: "+box[2])
print(""" """)
print("HP: "+str(HP))
print("Str: "+str(Str)+"   Mod: "+str((Str-10)/2))
print("Dex: "+str(Dex)+"   Mod: "+str((Dex-10)/2))
print("Con: "+str(Con)+"   Mod: "+str((Con-10)/2))
print("Int: "+str(Int)+"   Mod: "+str((Int-10)/2))
print("Wis: "+str(Wis)+"   Mod: "+str((Wis-10)/2))
print("Cha: "+str(Cha)+"   Mod: "+str((Cha-10)/2))
print(""" """)
print("Init: "+str((Dex-10)/2))
print(""" """)
print("BAB: "+str(BABB.pullBAB()))
print("Fort Save: "+str((Con-10)/2+BABB.pullFort()))
print("Ref Save: "+str(((Dex-10)/2)+BABB.pullRef()))
print("Will Save: "+str((Wis-10)/2+BABB.pullWill()))
print(""" """)
print("AC: "+str(((Dex-10)/2)+10+AC))
print("Flatfooted AC: "+str(10+AC))
print("Touch AC: "+str(((Dex-10)/2)+10+AC))
print(""" """)
#Weapon code needs work
#print("Weapon: "+weapons.weaponGrab())
print(""" """)
select = 1
skillValue = skills.pullSkillVals()
print("* = Class skill")
while(select<36):
  print(skills.pullSkillNames(select)+": "+"Total: "+str(skillValue[select][0])+" Mod: "+str(skillValue[select][1])+" Ranks: "+str(skillValue[select][2])+" Misc: "+str(skillValue[select][3]))
  select += 1
print(""" """)
if Class == "Bard" or Class == "Paladin" or Class == "Wizard" or Class == "Druid" or Class == "Sorcerer" or Class == "Ranger" or Class == "Cleric":
  print("Spell Slots")
  spellSlotNames = spellslots.pullSlotNames(Class)
  spellingSlots = spellslots.pullSpellSlots(CR-1,Class,Str,Dex,Con,Int,Wis,Cha)
  for i in range(0, len(spellingSlots)):
    print(spellSlotNames[i]+": "+str(spellingSlots[i]))
print(""" """)
print("Special Abilities")
for i in range(0, len(specialAbility)):
  print(specialAbility[i])
