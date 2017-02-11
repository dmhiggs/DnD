#stats & skills & saves ...... checks I guess
#    strength -- *Athletics
# +2 *dexterity -- *Acrobatics, *Sleight of Hand, *Stealth
#    constitution --
#    *intelligence -- Arcana, History, *Investigation, Nature, Religion
#    wisdom -- Animal Handling, *Insight, Medicine, *Perception, Survival
# +1 charisma -- *Deception, *Intimidation, *Performance, Persuasion
from math import *
import randomdice

class stat():
    basestat = 0
    basemod = 0

    istemp = False
    tempstat = 0
    tempmod = 0

    less = False
    more = False

    def __init__(self, racemod):
        self.race = racemod
        self.total = racemod
        self.oned6 = randomdice.die(6)
        self.twod6 = randomdice.die(6)
        self.threed6 = randomdice.die(6)
        return

    def rollstat(self):
        self.oned6.rolldie()
        self.twod6.rolldie()
        self.threed6.rolldie()
        self.basestat = self.oned6 + self.twod6 + self.threed6
        self.total = self.basestat + self.race
        self.basemod = floor((self.total - 10)/2)        
        return

    def setstat(self, number):
        self.basestat = number
        self.total = self.basestat + self.race
        self.basemod = floor((self.total - 10)/2)
        return
    
    def add(self, number):
        self.basestat = self.basestat + number
        self.total = self.basestat + self.race
        self.basemod = floor((self.total - 10)/2)
        return

    def tmod(self, temp):
        if temp == 0: ##wouldn't set it to 0 unless no more temp affect
            self.istemp = False
            self.tempstat = 0
            self.tempmod = 0
            self.total = self.basestat + self.race
            self.basemod = floor((self.total - 10)/2)
            self.less = False
            self.more = False
            return

        self.istemp = True
        self.tempstat = self.basestat + temp
        self.total = self.tempstat + self.race
        self.tempmod = floor((self.total - 10)/2)

        if self.tempstat > self.basestat:
            self.more = True
            self.less = False
        elif self.tempstat < self.basestat:
            self.more = False
            self.less = True
        else:
            self.istemp = False
            self.more = False
            self.less = False
            self.tempstat = 0
            self.tempmod = 0  
            self.total = self.basestat + self.race
            self.basemod = floor((self.total - 10)/2)
        return
        

class checks(): #for abilities and saves since they basically have same functions...

    def __init__(self, smod, jobskill):
        self.probonus = False
        self.expertise = False
        self.job = jobskill

        self.miscbonus = 0
        self.statmod = smod
        self.magicmod = 0
        self.tempmod = 0
        self.profb = 0
        self.prof = 2

        self.mod = smod
        self.passive = 10 + smod
        return

    #set if there's proficiency in skill/save
    def setprobonus(self, sprof):
        if self.job == False:
            return False
        self.probonus = sprof
        self.profb = 0
        self.changemod()
        if sprof == False:
            return False
        self.profb = self.prof
        self.changemod()
        return True

    #set if there's expertise in skill
    def setexpertise(self, exp):
        if self.probonus == False:
            return False
        
        self.expertise = exp
        self.profb = self.prof
        if exp:
            self.profb = 2*self.prof
        self.changemod()
        return True

    #for when level up and proficiency bonus increases
    def setprof(self, sprof):
        self.prof = sprof

        if self.expertise:
            temp = self.setexpertise(True)
        elif self.probonus:
            self.setprobonus(True)
        return

    #set magic mod
    def setmagic(self, magic):
        self.magicmod = self.magicmod + magic
        self.changemod()
        return
    
    #set temp mod
    def settemp(self, temp):
        self.tempmod = self.tempmod + temp

        if temp == 0: #setting to 0 is meant to mean that temp effect over...
            self.tempmod = 0

        self.changemod()
        return
    
    #set stat mod
    def setstat(self, stat):
        self.statmod = self.statmod + stat
        self.changemod()
        return
    
    #set misc mod
    def setmisc(self, misc):
        self.miscbonus = self.miscbonus + misc
        self.changemod()
        return
    
    #for when any part of the mod changed
    def changemod(self):
        self.mod = self.statmod + self.profb + self.miscbonus + self.magicmod + self.tempmod
        self.passive = 10 + self.mod
        return
