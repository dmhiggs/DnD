#BATTLE variables
    #advantage or disadvantage VARIABLE
    #SURPRISE VARIABLE -- if surprised then can't move or take action on first turn and can't take a reaction until that turn ends
    #current initiative VARIABLE
    #hidden VARIABLE

#inspiration on all screens?
#DONE on all play screens

#if not playing, then everything accessible/editable...and way to stop looking at that character and either make new or pick another

#on startup, choose CREATE NEW or one of the existing characters

#play screen
    #battle screen
    #interaction screen/explore
    #REST/HEAL
    #Inventory
    #DONE
        #add XP
            #if next level, level up

#battle screen
    #Get Initiative -- roll d20 + init MOD + MISC
    #TURN
    #HEAL/DAMAGE
    #DONE
        #if used ammo, ask how many recovered and edit amount in inventory

#interaction screen/explore
    #passive perception
    #inspiration
    #list languages, useful profs, useful feats
    #skill/ability checks screen
        #list by STAT MOD type
            #click on STAT type
                #click on specific ability and roll d20 + MOD
                #OR roll d20 + STAT MOD
        #HEAL/DAMAGE screen
        #DONE
    #saving throws screen
    #REST/HEAL screen
    #Inventory screen
        #Money amounts displayed
            #can click to add/subtract amount
        #Equipment displayed
            #Worn -- display all
                #armor
                    #click on item to move to another equipment/treasure list or sell
                        #apply all AC or any other change
                    #click + to take armor items from equipment/treasure list and put here
                        #OR add new item entirely
                        #then apply all AC or any other change
                #jewelry
                    #click on item to move to another equipment/treasure list or sell
                        #apply all AC or any other change
                    #click + to take armor items from equipment/treasure list and put here
                        #OR add new item entirely
                        #then apply all AC or any other change
            #Bag -- display first 10, Tools on top
                #click on item to remove, popup asks how much coin in return then adds that amount to money
                #click + to add item
                #click ... to see more items
                #click - to see less items
            #Beltpouch -- display all, Tools on top
                #click on item to remove, popup asks how much coin in return then adds that amount to money
                #click + to add item
                #click ... to see more items
                #click - to see less items
            #Weapons -- list all
                #click on item to remove, popup asks how much coin in return then adds that amount to money
                #click + to add item
            #Ammo -- list all
                #click on item to edit amount or remove item from list
                #click + to add item to list
        #Treasure displayed
            #click on item to remove, popup asks how much coin in return then adds that amount to money
            #click + to add item
            #click ... to see more items
            #click - to see less items
        #DONE
    #DONE

#death save screen
    #stable?
    #need 3 successes to stay ALIVE and become STABLE -- reset successes and failures to 0
    #need 3 failures to be DEAD -- reset successes and failures to 0
    #roll d20 + Magic + MISC
        #if >10, success
            #if 20, regain 1 HP -- reset successes and failures to 0
        #else, failure OR if roll 1 two failures
    #STABALIZE -- become STABLE -- reset successes and failures to 0
    #DAMAGE -- add failure, if CRIT add two failures, if damage - TEMP HP >= max HP then INSTANT DEATH
    #DONE

#rest/heal screen
    #short rest?
        #reset whatever is reset by SHORT
    #long rest?
        #reset whatever is reset by LONG
    #Healing potions?
    #USE POTION -- add whatever points up to max HP, subtract from inventory
    #HEAL -- add whatever points up to max HP --> if cast spell yourself, roll the points
    #HIT DICE -- use whatever available HIT DICE you want and add points up to max HP
    #DONE


#TURN screen
    #contest?
        #shoved?
            #if yes, roll STR(athletics) or DEX(acrobatics)
        #grappled?
            #if yes, roll STR(athletics) OR DEX(acrobatics)
        #grappler?
            #if yes, roll STR(athletics)
            #MOVE -- speed is halved unless creature is two or more sizes smaller
        #other skills maybe???
    #PRONE
        #CRAWL -- each foot of movement cost 1 extra foot
    #STANDUP -- cost 1/2 SPEED
    #REACTION (can't take another one until start of next turn):
        # Opportunity Attack
    # MOVE up to SPEED &&& take one ACTION -- either can be first
        # ACTION:
            # Interact w/ Object or hand object to another character
            # Use Potion -- roll HP healed, remove from inventory
            # First Aid -- DC 10 WIS(Medicine) check
            # Attack -- ranged or melee
            # Cast a spell
            # Dash -- gain extra movement for current turn equal to SPEED
            # Disengage -- movement doesn't provoke opportunity attacks for rest of the turn
            # Dodge -- until start of your next turn, attack rolls against you have DIS if can see attacker & make DEX save with ADV -- lose benefit if incapacitated or SPEED drops to 0
            # Help -- creature you aid gains ADV on next ability check it makes to perform task you're helping with, provided it makes check before start of your next turn
            # Hide -- make DEX(stealth) check to hide
                #if succeed then
                    #??? cover???
            # Ready Action
            # Search -- WIS(perception) or INT(investigation) check
        # MOVE if did not already go to max
        # BONUS ACTION
    #END TURN


#ATTACK -- attack screen
    #have ADV? or DIS?
    #hidden? -- gets ADV
    #Sneak Attack?
    #Off hand?
    #Weapon Attack
        #Choose Weapon
            #Improvised?
            #if ranged Choose Ammo and Choose Short/Normal/Long range
            #Roll d20(s) + MOD + Prof Bonus + Magic + MISC
                #if LUCKY, reroll 1 once per die
                #if CRIT, CRIT true
            #select HIT or MISS
            #Roll Damage + MOD + Magic + MISC + Sneak Attack
                #if CRIT, Roll Damage die again and Sneak Attack again and add to damage
            #if ranged, loose one AMMO
    #Unarmed Strike -- punch, kick, head butt, etc
        #Roll d20(s) + STR + Magic + MISC
            #if LUCKY, reroll 1 once per die
            #if CRIT, CRIT true
        #select HIT or MISS
        #Roll Damage + 1 + STR + Magic + MISC + Sneak Attack
            #if CRIT, Roll Damage die again and Sneak Attack again and add to damage
    #Grapple
        #roll STR(athletics)
    #Shoving a creature -- to knock prone or push away target that is 1 or less sizes larger w/in reach
        #roll STR(athletics)
    #DONE


#SAVING THROWS screen
    #half cover? -- +2 bonus to AC and DEX saving throws
    #three-quarters cover? -- +5 bonus to AC and DEX saving throws
    #I guess whatever saving throw d20 + MOD + Prof Bonus + Magic + MISC + cover
    #access to death screen, maybe
    #DONE


#HEALING/DAMAGE
    #types -- Acid, Bludgeoning, Cold, Fire, Force, Lightning, Necrotic, Piercing, Poison, Psychic, Radiant, Slashing, Thunder
    #resistance? -- Half Damage even if multiple resistance applies
    #vulnerability? -- Double Damage even if multiple vulnerabilities applies
    #magic altered? -- Applies First
        #set whether it adds or subtracts specific number
    #at half of more of HP? -- no signs of injury
        #else, signs of wear, cuts, bruises
    #at 0 HP? -- bleeding injury or other trauma or unconscious --> go to death screen
    #TEMP HP? -- set amount
    #Select HEAL or DAMAGE
        #if HEAL, add X amount of points up to current max HP
        #if DAMAGE, X=X-TEMP HP then subtract X amount of points until hits 0 HP
            #if hit 0 HP, go to death screen
                #if left over damage >= max HP, INSTANT DEATH
                    #mark character as DEAD
    #DONE, go back to prev screen
