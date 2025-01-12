#2021
# Can Nova escape the wolves and find her way home? choose from options and see if you can help her!

# HOMEWARD BOUND + 
#Set values 
lucky_charm = False
escaped_doggo = False
starved = False
sitting_duck = False
lovers = False
harvested = False
final_trade = False
fighter = False
lone_wolf = False
restart = True
total_game_played = 0
total_ending = 0
print("\n\n| Welcome to Homeward Bound+ |")
while restart == True:
    difficulty_distance = 0
    distance = 200
    hunger = 7
    stamina = 7
    snacks = 3
    wolve_distance = 20
    import random
    whole = "{:.0f}"
    snackshack = 0
    quitgame = False
    endgame = False
    snackshack_ending = False
    peace_nigotiated = False
    fight_end = False
    boss_fight_notice = 0
    peace_notice = 0
    difficulty_display = ""
    perk_display = ''
    difficulty = input("\nEasy/Normal/Hard/Brutal\nSelect a difficulty (E/N/H/B): ")
    #Hidden diffculty created for testing 
    if difficulty.upper() == "T":
        wolve_distance = 10000000000000
        snacks = 100000000000
        stamina = 300000000000
        hunger = 300000000
        distance = 100
        difficulty_distance = 100
        difficulty_display = "Test"
        print("\nWelcome to TEST MODE \nFeel free to explore all the features\n_____________________________")
    elif difficulty.upper() == "E":
        wolve_distance = 25
        difficulty_distance = 185
        distance = 175
        difficulty_display = "Easy"
        print("\nDifficluty Set to \"Easy\" \nNova has 15KM less to run, Wolves are set back 5KM\n_____________________________")
    elif difficulty.upper() == "N":
        wolve_distance = 20
        difficulty_distance = 200
        distance = 200
        difficulty_display = "Normal"
        print("\nDifficluty Set to \"Normal\"\n_____________________________")
    elif difficulty.upper() == "H":
        wolve_distance = 15
        difficulty_distance = 205
        distance = 205
        difficulty_display = "Hard"
        print("\nDifficluty Set to \"Hard\"\nNova has 5KM more to run, Wolves are set forward by 5KM\n_____________________________")
    elif difficulty.upper() == "B":
        wolve_distance = 10 
        difficulty_distance = 215
        distance = 215
        difficulty_display = "Brutal"
        print("\nDifficluty Set to \"Brutal\"\nNova has 15KM more to run, Wolves are set forward by 10KM\n_____________________________")
    else:
        print("\nDid not choose any presented difficulty options \nDifficulty set to \"Normal\" on default\n_____________________________")
    perk = input("\nPlease choose a perk: \nA. +Speed  \nB. +Luck \nC. +Health\nSelection: ")
    if perk.upper() == "A":
        perk_display = "Speed+"
        print("\nSpeed Perk selected")
    elif perk.upper() == "B":
        perk_display = "Luck+"
        print("\nLuck Perk selected")
    elif perk.upper() == "C":
        perk_display = "Health+"
        print("\nHealth Perk selected")
    else:
        print("\nNo perk selected")
    #The speed perk increases the bottom of the range of the travel distance, and the luck perk increases the chances of finding a snack shack and decrease the chance of Oversleeping and Tripping. The Health perk gives you +2HP in the boss fight.     
    print("_____________________________\n\nSurvive your journey home and outrun the wolves")
    while endgame == False:
        #Actions 
        if distance < 50 and boss_fight_notice == 0:
            action = input("\n ====================== \n FIGHT OPTION UNLOCKED \n ====================== \n\nNova is "+str(distance)+"KM away from home.\nA. Eat a Snack\nB. Run at moderate speed\nC. Gallop at full speed\nD. Stop and Rest\nE. Status Check\nF. Fight \nQ. Quit\nYour Choice: ")
            boss_fight_notice = boss_fight_notice + 1
        elif distance < 50 and boss_fight_notice == 0:
            ("\nNova is "+str(distance)+"KM away from home.\nA. Eat a Snack\nB. Run at moderate speed\nC. Gallop at full speed\nD. Stop and Rest\nE. Status Check\nF. Fight \nQ. Quit\nYour Choice: ")
        else:
            action = input("\nNova is "+str(distance)+"KM away from home.\nA. Eat a Snack\nB. Run at moderate speed\nC. Gallop at full speed\nD. Stop and Rest\nE. Status Check\nQ. Quit\nYour Choice: ")
        if action.upper() == "A":
            if snacks <=0:
                print("You have no snacks left, try again?")
            else:
                hunger = 7
                snacks = snacks-1
                wolve_travell = random.randrange(5,15)
                wolve_distance = wolve_distance - wolve_travell
        elif action.upper() == "B":
            if perk.upper() == "A":
                travell = random.randrange(8,11)
            else:
                travell = random.randrange(7,11)
            distance = distance - travell
            hunger = hunger - 1
            stamina = stamina - 0
            wolve_distance = wolve_distance + travell
            wolve_travell = random.randrange(5,15)
            wolve_distance = wolve_distance - wolve_travell
            print("\nNova travelled",travell,"kilometers")
            #Snack Shack Event
            if perk.upper() == "B":
                snack_shack = random.randrange(24)
            else: 
                snack_shack = random.randrange(25)
            if snack_shack == 1:
                print("\n==========================\nNOVA FOUND A SHACK SHACK!!\n==========================\nStamina and Hunger levels reset to max. One more snack added to your collection")
                stamina = 7
                hunger = 7
                snacks = snacks + 1
                snackshack = snackshack + 1
        elif action.upper() == "C":
            if perk.upper() == "A":
                travell = random.randrange(15,18)
            else:
                travell = random.randrange(14,18)
            #Tripping Event
            if perk.upper() == "B":
                trip = random.randrange(31)
            else:
                trip = random.randrange(30)
            if trip == 1:
                print("\n==============================\nNOVA TRIPPED WHILE GALLOPING!!\n==============================\nDistance travelled halved")
                travell = travell/2
            distance = distance - travell
            hunger_used = random.randrange(2,4)
            hunger = hunger - hunger_used
            stamina = stamina - 1
            wolve_distance = wolve_distance + travell
            wolve_travell = random.randrange(5,15)
            wolve_distance = wolve_distance - wolve_travell
            print("\nNova travelled",travell,"kilometers")
            #Snack Shack Event
            if perk.upper() == "B":
                snack_shack = random.randrange(24)
            else: 
                snack_shack = random.randrange(25)
            if snack_shack == 1:
                print("\n==========================\nNOVA FOUND A SHACK SHACK!!\n==========================\nStamina and Hunger levels reset to max. One more snack added to your collection")
                stamina = 7
                hunger = 7
                snacks = snacks + 1
                snackshack = snackshack + 1
        elif action.upper() == "D":
            stamina = 7
            #Over Resting Event
            if perk.upper() == "B":
                over_rest = random.randrange(26)
            else:
                over_rest = random.randrange(25)
            if over_rest == 1:
                print("\n=====================\nNOVA SLEPT TOO MUCH!!\n=====================\nWolves got 3KM closer, Stamina level overcharged to 9")
                wolve_distance = wolve_distance - 3
                stamina = 9
            wolve_travell = random.randrange(5,15)
            wolve_distance = wolve_distance - wolve_travell
            print("\nNova feels refreshed, but the wolves are getting closer...")
        elif action.upper() == "E":
            if difficulty.upper() == "H" or difficulty.upper() == "B":
                print("\n_____________________________\n\nDistance Remaining:",distance,"KM\nSnacks Left:",snacks," \nThe wolves are ",wolve_distance,"KM away from you\n_____________________________")
            else:
                print("\n_____________________________\n\nDistance Remaining:",distance,"KM\nSnacks Left:",snacks," \nThe wolves are ",wolve_distance,"KM away from you")
                print("Hunger Level: ",hunger,"\nStamina Level: ",stamina,"\n_____________________________")
            #Boss fight with the Wolf Pack Leader
            #Set HP for both the Leader and Nova, you can choose to bite, kick, or heal for a random value in a range, the wolf will do a move randomly. Whoever's health reaches 0 first loses, but if both reach 0 at the same time, Nova still lose. 
        elif action.upper() == "F":
            if distance > 50:
                print("\nNova is too far away from home to fight \nthis option unlocks when you are within 50KM of home\n")
            else:
                print("\nNova turned around to fight the wolves....")
                wolve_health = 20
                if perk.upper() == "C": 
                    nova_health = 25
                else:
                    nova_health = 20
                fight_end = False
                win = False
                tie = False
                while fight_end == False:
                    print("\n\n   WOLF PACK LEADER \n\t",wolve_health,"HP")
                    print("\n\n\t",nova_health,"HP\n\t NOVA\n")
                    if wolve_health < 5 and nova_health > wolve_health + 3 and peace_notice == 0:
                        fight = input("\n ====================== \n PEACE OPTION UNLOCKED \n ======================\n\nA. Bite\nB. Kick\nC. Heal\nD. Peace\nChoose Nova's Move: ")
                        peace_notice = peace_notice+1
                    elif wolve_health < 5 and nova_health > wolve_health + 3 and peace_notice == 1:
                        fight = input("A. Bite\nB. Kick\nC. Heal\nD. Peace\nChoose Nova's Move: ")
                    else:
                        fight = input("A. Bite\nB. Kick\nC. Heal\nChoose Nova's Move: ")
                    if fight.upper() == "A":
                        print("\nNova bit the leader! \nWolf Pack Leader took 2 Damage!")
                        wolve_health = wolve_health - 2
                        wolfmove = random.randrange(1,6)
                        #Reduced the chances of Healing to make the fight more enjoyable 
                        if wolfmove == 1 or wolfmove == 2:
                            wolf_dmg = random.randrange(2,3)
                            nova_health = nova_health - wolf_dmg
                            print("\nWolf Pack Leader bit Nova! \nNova took",wolf_dmg,"Damage!")
                        elif wolfmove == 3 or wolfmove == 4:
                            wolf_dmg = random.randrange(1,5)
                            print("\nWolf Pack Leader kicked Nova! \nNova took",wolf_dmg,"Damage!")
                            nova_health = nova_health - wolf_dmg
                        elif wolfmove == 5:
                            wolve_health = wolve_health + 2
                            print("\nWolf Pack Leader Healed for 2 HP!")
                    elif fight.upper() == "B":
                        kick = random.randrange(2,5)
                        wolve_health = wolve_health - kick
                        print("\nNova bit the leader! \nWolf Pack Leader took",kick,"Damage!")
                        wolfmove = random.randrange(1,6)
                        if wolfmove == 1 or wolfmove == 2:
                            wolf_dmg = random.randrange(2,3)
                            nova_health = nova_health - wolf_dmg
                            print("\nWolf Pack Leader bit Nova! \nNova took",wolf_dmg,"Damage!")
                        elif wolfmove == 3 or wolfmove == 4:
                            wolf_dmg = random.randrange(1,5)
                            print("\nWolf Pack Leader kicked Nova! \nNova took",wolf_dmg,"Damage!")
                            nova_health = nova_health - wolf_dmg
                        elif wolfmove == 5:
                            wolve_health = wolve_health + 3
                            print("\nWolf Pack Leader Healed for 3 HP!")
                    elif fight.upper() == "C":
                        heal = random.randrange(2,3)
                        nova_health = nova_health + heal
                        print("\nNova healed for",heal,"HP!")
                        wolfmove = random.randrange(1,6)
                        if wolfmove == 1 or wolfmove == 2:
                            wolf_dmg = random.randrange(2,3)
                            nova_health = nova_health - wolf_dmg
                            print("\nWolf Pack Leader bit Nova! \nNova took",wolf_dmg,"Damage!")
                        elif wolfmove == 3 or wolfmove == 4:
                            wolf_dmg = random.randrange(1,5)
                            print("\nWolf Pack Leader kicked Nova! \nNova took",wolf_dmg,"Damage!")
                            nova_health = nova_health - wolf_dmg
                        elif wolfmove == 5:
                            wolve_health = wolve_health + 3
                            print("\nWolf Pack Leader Healed for 3 HP!")  
                    elif fight.upper() == "D":
                        #Peace Deal (20% chance that Scotia rejects peace deal)
                        if wolve_health > 5 or nova_health <= wolve_health + 3:
                            print("Nova cannot negotiate peace since she does not have an noticable advantange against the Wolf Pack Leader")
                        else: 
                            peace = random.randrange(1,6)
                            if peace == 1 or peace == 2 or peace == 3 or peace == 4:
                                peace_nigotiated = True
                                print("\nThe wolf pack's leader \"Scotia\" accepted Nova's peace deal.  \nNova wandered home safely with the protection of the Wolf Pack")
                                fight_end = True
                                endgame = True
                            elif peace == 5:
                                peace_nigotiated = False
                                print("\nThe wolf pack's leader \"Scotia\" ignored Nova's peace deal and charged at her\nWith no other choices left, Nova killed Scotia")
                                fight_end = True
                                endgame = True
                                win = True
                    #Boss Fight ending results 
                    if wolve_health <= 0 and nova_health <=0:
                        fight_end = True
                        tie = True
                        endgame = True
                        print("\nAfter a brutal battle... \nNova and the Wolf Pack Leader both ripped each other open")
                    elif wolve_health <= 0:
                        fight_end = True
                        win = True
                        endgame = True
                        print("\nAfter a brutal battle... \nNova walked out victorious, and with all the wolves' respect, \nShe became the new Wolf Pack Leader")
                    elif nova_health <= 0:
                        fight_end = True
                        win = False
                        endgame = True
                        print("\nAfter a brutal battle... \nNova has been defeated and killed by the Wolf Pack Leader")       
        elif action.upper() == "Q":
            endgame = True
            quitgame = True
        else:
            print("\nPlease choose from [A|B|C|D|E|F|Q]")
        #Warnings
        if stamina < 4:
            print("Nova is getting really tired....")
        if hunger < 4:
            print("Nova is getting really hungry....")
        if wolve_distance < 10:
            print("The wolves are getting close!")
        if (distance <= 0) or (stamina <= 0) or (hunger <= 0) or (wolve_distance <=0):
            endgame = True
        elif snackshack > 2: #If Nova encounters 3 or more snack shacks, a win condition is met
            endgame = True
            snackshack_ending = True
            print("\nNova's luck is unbeatable!\nShe has finally found a snack shack strong enough to withstand the wolves ")
    if quitgame == True:
        print("\nYou have terminated the game\nMaybe try again another day?")
    #ending conditions 
    if snackshack_ending == True and snackshack > 2:
        print("\nNOVA FOUND A SUITABLE SNACK SHACK TO HIDE IN")
        print("--------| THE \"LUCKY CHARM\" ENDING |--------")
        #added checks to see if you completed the ending or not
        if lucky_charm == False:
            total_ending = total_ending + 1
            lucky_charm = True
    elif distance <= 0:
        print("\nNOVA MADE IT HOME SAFE AND ESCAPED THE WOLVES!")
        print("--------| THE \"ESCAPED DOGGO\" ENDING |--------")
        if escaped_doggo == False:
            total_ending = total_ending + 1
            escaped_doggo = True        
    elif stamina <= 0: 
        print("\nNOVA PASSED OUT FROM EXHAUSTION AND GOT EATEN")
        print("--------| THE \"SITTING DUCK\" ENDING |--------")
        if sitting_duck == False:
            total_ending = total_ending + 1
            sitting_duck = True    
    elif hunger <= 0:
        print("\nNOVA PASSED OUT FROM HUNGER AND GOT EATEN")
        print("--------| THE \"STARVED\" ENDING |---------")
        if starved == False:
            total_ending = total_ending + 1
            starved = True    
    elif peace_nigotiated == True:
        print("\nNOVA AND SCOTIA BECAME ALLIES")
        print("---| THE \"LOVERS\" ENDING |---")
        if lovers == False:
            total_ending = total_ending + 1
            lovers = True    
    elif wolve_distance <= 0:
        print("\nTHE WOLVES CAUGHT UP AND MURDERED NOVA")
        print("------| THE \"HARVESTED\" ENDING |------")
        if harvested == False:
            total_ending = total_ending + 1
            harvested = True 
    elif fight_end == True and tie == True:
        print("\nNOVA AND THE WOLF PACK LEADER BOTH DIED")
        print("-----| THE \"FINAL TRADE\" ENDING |------")
        if final_trade == False:
            total_ending = total_ending + 1
            final_trade = True 
    elif fight_end == True and win == True:
        print("\nNOVA FAUGHT AND REPLACED THE WOLF PACK LEADER!")
        print("----------| THE \"LONE WOLF\" ENDING |----------")
        if lone_wolf == False:
            total_ending = total_ending + 1
            lone_wolf = True 
    elif fight_end == True and win == False:
        print("\nTHE WOLF PACK LEADER HAS DEFEATED NOVA!")
        print("-------| THE \"FIGHTER\" ENDING |--------")
        if fighter == False:
            total_ending = total_ending + 1
            fighter = True    
    total_game_played = total_game_played + 1
    if total_ending <= 8:
        print("\n\n[Game Summary]\nGames Played: ",total_game_played,"\nEndings Achieved: ",total_ending,"/ 9")
        restartinput=input("\nWould you like to restart the game and unlock other endings (Y/N)? ")
        if restartinput.upper() == "Y":
            print("\n| Welcome to another game of Homeward Bound+ |")
        elif restartinput.upper() == "N":
            print("\nThanks for playing!")
            restart = False
    else:
        print("\n\nYou have achieved all 9 endings for [Homeward Bound+]\nThanks for Playing!")
        restart = False

# Updates and Additions:

# Base Game
# Difficulty settings
# Test Mode
# Random Events (Trip, OverSleep)
# Wolf Pack Leader Boss Fight
# More Endings 
# Perks
# Restart Option & End Game Summary
