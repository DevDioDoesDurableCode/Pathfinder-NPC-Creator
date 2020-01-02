from random import randint
godList = ["Erastil","Iomedae","Torag","Sarenrae","Shelyn","Desna","Cayden Cailean","Abadar","Irori","Gozreh","Pharasma","Nethys","Gorum","Calistria","Asmodeus","Zon-Kuthon","Urgathoa","Norgorber","Lamashtu","Rovagug"]
godDomain = [["Animal", "Community", "Good", "Law", "Plant"],["Glory", "Good", "Law", "Sun", "War"],["Artifice", "Earth", "Good", "Law", "Protection"],["Fire", "Glory", "Good", "Healing", "Sun"],["Air", "Charm", "Good", "Luck", "Protection"],["Chaos", "Good", "Liberation", "Luck", "Travel"],["Chaos", "Charm", "Good", "Strength", "Travel"],["Earth", "Law", "Nobility", "Protection", "Travel"],["Healing", "Knowledge", "Law", "Rune", "Strength"],["Air", "Animal", "Plant", "Water", "Weather"],["Death", "Healing", "Knowledge", "Repose", "Water"],["Destruction", "Knowledge", "Magic","Protection", "Rune"],["Chaos", "Destruction", "Glory", "Strength", "War"],["Chaos", "Charm", "Knowledge", "Luck", "Trickery"],["Evil", "Fire", "Law", "Magic", "Trickery"],["Darkness", "Death", "Destruction", "Evil", "Law"],["Death", "Evil", "Magic", "Strength", "War"],["Charm", "Death", "Evil", "Knowledge", "Trickery"],["Chaos", "Evil", "Madness", "Strength", "Trickery"],["Chaos", "Destruction", "Evil", "War", "Weather"]]
godAlignment = [["Lawful","Good"],["Lawful","Good"],["Lawful","Good"],["Neutral","Good"],["Neutral","Good"],["Choatic","Good"],["Choatic","Good"],["Lawful","Neutral"],["Lawful","Neutral"],["Neutral","Neutral"],["Neutral","Neutral"],["Neutral","Neutral"],["Choatic","Neutral"],["Choatic","Neutral"],["Lawful","Evil"],["Lawful","Evil"],["Neutral","Evil"],["Lawful","Evil"],["Choatic","Evil"],["Choatic","Evil"]]
wizSchools = ["Abjuration" ,"Conjuration","Divination" ,"Enchantment","Evocation" ,"Illusion" ,"Necromancy" ,"Transmutation" ,"Universalist"]
wizBondage = ["Wand", "Staff", "Ring","Weapon","Amulet"]
wizFam = ["Bat", "Cat", "Hawk", "Lizard", "Monkey", "Owl", "Rat", "Raven", "Viper", "Toad", "Weasel"]
socBloodLine = ["Aberrant", "Abyssal", "Arcane", "Celestial", "Destined", "Draconic", "Elemental", "Fey", "Infernal", "Undead"]
socBloodLineSkill = [14,21,0,11,17,24,21,19,5,22]
favorEnemy = ["Aberration", "Humanoid (other subtype)","Animal", "Magical beast","Construct", "Monstrous humanoid","Dragon", "Ooze","Fey", "Outsider (air)","Humanoid (aquatic)", "Outsider (chaotic)","Humanoid (dwarf)", "Outsider (earth)","Humanoid (elf)", "Outsider (evil)","Humanoid (giant)", "Outsider (fire)","Humanoid (goblinoid)", "Outsider (good)","Humanoid (gnoll)", "Outsider (lawful)","Humanoid (gnome)", "Outsider (native)","Humanoid (halfling)", "Outsider (water)","Humanoid (human)", "Plant","Humanoid (orc)", "Undead","Humanoid (reptilian)", "Vermin"]
favorTerrain = ["Cold","Desert","Forest","Jungle","Mountain","Plains","Planes","Swamp","Underground","Urban","Water"]
specialPackage = {}
def classExtras(Class, level):
  global godlist, domains, wizSchools, wizBondage, wizFam, socBloodLine, socBloodLineSkill,favorEnemy, favorTerrain, specialPackage
  if Class == "Barbarian":
    specialPackage[0] = "Rage (Ex)"
    if level >= 2 and level < 5:
      specialPackage[1] = "Uncanny Dodge (Ex)"
  if Class == "Cleric":
    godnumb = randint(0,len(godList)-1)
    god = godList[godnumb]
    alignmentMarker = randint(0,1)
    alignment = godAlignment[godnumb][alignmentMarker]
    domain = godDomain[godnumb][randint(0, len(godDomain[godnumb])-1)]
    package = [god,domain,alignment,str(alignmentMarker)]
  if Class == "Ranger":
    favorered = ""
    favoreredTerr = ""
    oneItemMoreEnemy = False
    oneItemMoreTerr = False
    tempFavorList = [""]*((level/5)+1)
    if level >= 3:
      tempFavorListTerr = [""]*(((level-3)/5)+1)
      for i in range(0, len(tempFavorListTerr)):
        tempFavorListTerr[i] = favorTerrain[randint(0, len(favorTerrain)-1)]
        favoreredTerr = favoreredTerr+tempFavorListTerr[i]+" " 
        if i is not len(tempFavorListTerr)-1:
          favoreredTerr = favoreredTerr+", "
          oneItemMoreTerr = True
    else:
      favoreredTerr = "1"
    
    for i in range(0, len(tempFavorList)):
      tempFavorList[i] = favorEnemy[randint(0, len(favorEnemy)-1)]
      favorered = favorered+tempFavorList[i]+" " 
      if i is not len(tempFavorList)-1:
        favorered = favorered+", "
        oneItemMoreEnemy = True
    package = [favorered, oneItemMoreEnemy,favoreredTerr,oneItemMoreTerr]
  if Class == "Sorcerer":
    bloodLineNumb = randint(0, len(socBloodLine)-1)
    bloodLine = socBloodLine[bloodLineNumb]
    bloodlineSkill = socBloodLineSkill[bloodLineNumb]
    if bloodLine == "Arcane":
      tempBloodList = [14,15,16,17,18,19,20,21,22]
      bloodlineSkill = tempBloodList[randint(0, len(tempBloodList)-1)]
    package = [bloodLine,bloodlineSkill]
  if Class == "Wizard":
    schoolNumb = randint(0, len(wizSchools)-1)
    school = wizSchools[schoolNumb]
    count = 0
    antiSchool = ""
    antiSchoolTemp = ""
    stuckWith = randint(0,1)
    bondage = wizBondage[randint(0, len(wizSchools)-1)]
    Fam = wizFam[randint(0, len(wizSchools)-1)]
    if stuckWith == 0:
      bonded = bondage
      bondChoose = 0
    else:
      bonded = Fam
      bondChoose = 1
    if school != "Universalist":
      while count < 2:
        antiSchoolTemp = wizSchools[randint(0, len(wizSchools)-1)]
        if antiSchoolTemp != school and antiSchoolTemp != "Universalist":
          antiSchool = antiSchool+" "+antiSchoolTemp
          count += 1
    else:
      antiSchool = "None"
    package = [school,antiSchool,bonded,bondChoose]
  return package