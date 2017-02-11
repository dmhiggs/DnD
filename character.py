#character stuff
import checks
import randomdice
from math import *

class Character():
    #info text that isn't accessed that often
    name = ""
    alignment = ""
    personality = ""
    ideal = ""
    bond = ""
    flaw = ""

    #important for creation
    race = "hobbit" #when make other races, will implement change to a object that affects stat numbers and available feats
    job = "Rogue" #same plan as the race value
    background = "Sailor/Corsair" #same plan

    #numbers/booleans
    inspiration = False #can either have or not -- gives adv on attack, save, ability OR give to another PC
    level = 0
    xp = 0
    proficiency = 0
    passiveperception = 0 #any passive check is 10+MODs
    lifestyle = 0
    size = 0
    attunement = 0
    maxattunement = 0
    exhaustion = 0
    station = 0
    hp = 0
    thp = 0
    ac = 0
    initiative = 0
    speed = 25

    #stats & skills & saves
    strength = checks.stat(0)
    dexterity = checks.stat(2)
    constitution = checks.stat(0)
    intelligence = checks.stat(0)
    wisdom = checks.stat(0)
    charisma = checks.stat(1)

    strength_save = checks.checks(strength.basemod, False)
    dexterity_save = checks.checks(dexterity.basemod, True)
    constitution_save = checks.checks(constitution.basemod, False)
    intelligence_save = checks.checks(intelligence.basemod, True)
    wisdom_save = checks.checks(wisdom.basemod, False)
    charisma_save = checks.checks(charisma.basemod, False)

    athletics = checks.checks(strength.basemod, True)
    
    acrobatics = checks.checks(dexterity.basemod, True)
    sleight = checks.checks(dexterity.basemod, True)
    stealth = checks.checks(dexterity.basemod, True)

    arcana = checks.checks(intelligence.basemod, False)
    history = checks.checks(intelligence.basemod, False)
    investigation = checks.checks(intelligence.basemod, True)
    nature = checks.checks(intelligence.basemod, False)
    religion = checks.checks(intelligence.basemod, False)

    animalhandling = checks.checks(wisdom.basemod, False)
    insight = checks.checks(wisdom.basemod, True)
    medicine = checks.checks(wisdom.basemod, False)
    perception = checks.checks(wisdom.basemod, True)
    survival = checks.checks(wisdom.basemod, False)

    deception = checks.checks(charisma.basemod, True)
    intimidation = checks.checks(charisma.basemod, True)
    performance = checks.checks(charisma.basemod, True)
    persuasion = checks.checks(charisma.basemod, False)
    
    #languages
    languages = ["Common", "Halfling", "Thieves' Cant"]
    
    #tool proficiencies
    tools = ["Thieves' Tools", "Navigator's Tools"]
    
    #armor proficiencies
    armor = ["Light Armor"]
    
    #weapon proficiencies
    weapon = ["Simple", "Crossbow, Hand", "Longsword", "Shortsword", "Rapier", "Dagger", "Scimitar"]
    
    #vehicle proficiencies
    vehicle = ["Vehicles (Water)"]
    
    #Hit Dice
    hd = "d8"
    hdnum = 1
    
    #inventory
    #Features










class hitdice():
    def __init__(self, num, hd, mod):
        self.dicenum = num
        self.statmod = mod
        self.hitd = hd
        self.pos = " +"
        if mod < 0:
            self.pos = " -"
        self.string = str(num) + hd + self.pos + mod
        self.dice = []
        self.used = 0

        #set them all as 0...as they're used, mark as used by changing to 1
        for i in range(num):
            self.dice.append(0)

        return

    def add_die(self):
        self.dicenum = self.dicenum + 1
        self.dice.append(0)
        self.string = str(self.dicenum) + self.hitd + self.pos + self.statmod
        return

    def change_mod(self, mod):
        self.statmod = mod
        self.pos = " +"
        if mod < 0:
            self.pos = " -"
        self.string = str(self.dicenum) + self.hitd + self.pos + self.statmod
        return

    def change_die(self, num):
        self.dicenum = num
        for i in range(abs(self.dicenum - num)):
            self.dice.append(0)
        self.string = str(self.dicenum) + self.hitd + self.pos + self.statmod
        return

    def use_die(self):
        pass

    def clear_die(self):
        pass
