import random
# stats is list with base stats, ordered attack, defense, hp, speed
# moveset is dictionary of Move Class objects
# expTot is total exp earned
# class Fighter(stats, moveset, expTot):
#     def __init__(self, stats, moveset, expTot):
#         self.expTot = expTot
#         self.level = findLevel(self.expTot)
#         self.atk = (stats[0] // 20 + 1) * self.level
#         self.dfs = (stats[1] // 20 + 1) * self.level
#         self.spd = (stats[2] // 20 + 1) * self.level
#         self.hp = (stats[3] // 20 + 1) * self.level
#         self.tempAtk = self.atk
#         self.tempDef = self.dfs
#         self.tempSpd = self.spd
#         self.tempHp = self.hp
#         self.move1 = moveset[0]
#         self.move2 = moveset[1]
#         self.move3 = moveset[2]
#         self.move4 = moveset[3]

#     def replaceMove(self, moveToReplace):
#         # user picks move to replace, move position is assigned to moveSelected, cancel button = 0
#         moveSelected = 5
#         if moveSelected == 0:
#             moveSelected #do the update thingy to resume to game
#         elif moveSelected == 1:
#             self.move1 = moveToReplace
#         elif moveSelected == 2:
#             self.move2 = moveToReplace
#         elif moveSelected == 3:
#             self.move3 = moveToReplace
#         elif moveSelected == 4:
#             self.move4 = moveToReplace

# def findLevel(expTot):
#     level =  0
#     level = expTot // 1000
#     return (level + 1)

# class Move(moveDetails):
#     def __init__(self, moveDetails):
#         self.bp = moveDetails[0]
#         self.acc = moveDetails[1]
#         self.pp = moveDetails[2]
#         self.effect = moveDetails[3]
#         self.priority = moveDetails[4]
#         self.learnLvl = moveDetails[5]

# lebronStats = [85, 75, 60, 70]

# lebronMoves = {
#     "Chasedown Block": Move([0, 100, 10, 1, 1, 0]),
#     "Yabadabadoo Old Navy": Move([0, 50, 20, 2, 0, 0]),
#     "Cleveland!! This is for You!": Move([0, 100, 15, 3, 0, 0]),
#     "Tomohawk Dunk": Move([100, 90, 10, 4, 0, 0])
# }

# """
# Effects list (to implement later)
# 1 - The user runs with high speeds and blocks the enemies attack, this move has priority. If this move is repeated consecutively, its accuracy is halved. 
# 2 - The user sings with such confidence putting the opponent in a dream-like state causing them to fall asleep.
# 3 - Increases attack stat by 1 stage - maxes out at 6
# 4 - This move has a 20% chance of lowering the opponents defense by 1 stage. 
# """

# def speedCalc(fighter1, fighter2, movef1, movef2):
#     if (movef1.priority == movef2.priority):
#         if (fighter1.spd > fighter2.spd):
#             return True
#         elif (fighter1.spd == fighter2.spd):
#             speedTie = random.randint(1,2)
#             if speedTie == 1:
#                 return True
#             elif speedTie == 2:
#                 return False
#         elif (fighter1.spd < fighter2.spd):
#             return False
#     elif (movef1.priority > movef2.priority):
#         return True
#     elif (movef1.priority < movef2.priority):
#         return True
    
# def damageCalc(attacker, target, move):
#     rng = random.randint(1,100)
#     if rng > 95:
#         criticalHit = 1.5
#     else:
#         criticalHit = 1
#     damage = (((2 * attacker.level) / 5) * move.bp * (attacker.tempAtk / target.tempDef)) * criticalHit / 50 + 2
#     print(damage)
#     target.tempHP -= damage
#     #if target.tempHP < 0:
#         # call method for ending battle loop
        

class Fighter:
    def __init__(self, stats, moveset, expTot):
        self.expTot = expTot
        self.level = findLevel(self.expTot)
        self.atk = (stats[0] // 20 + 1) * self.level
        self.dfs = (stats[1] // 20 + 1) * self.level
        self.spd = (stats[2] // 20 + 1) * self.level
        self.hp = (stats[3] // 20 + 1) * self.level
        self.accuracy = 1.0
        self.tempAcc = self.accuracy
        self.tempAtk = self.atk
        self.tempDef = self.dfs
        self.tempSpd = self.spd
        self.tempHp = self.hp
        
        self.move1bp = moveset[0][0]
        self.move1acc = moveset[0][1]
        self.move1pp = moveset[0][2]
        self.move1effect = moveset[0][3]
        self.move1priority = moveset[0][4]
        self.move1learnLvl = moveset[0][5]
        self.move1name = moveset[0][6]

        self.move2bp = moveset[1][0]
        self.move2acc = moveset[1][1]
        self.move2pp = moveset[1][2]
        self.move2effect = moveset[1][3]
        self.move2priority = moveset[1][4]
        self.move2learnLvl = moveset[1][5]
        self.move2name = moveset[1][6]
        
        self.move3bp = moveset[2][0]
        self.move3acc = moveset[2][1]
        self.move3pp = moveset[2][2]
        self.move3effect = moveset[2][3]
        self.move3priority = moveset[2][4]
        self.move3learnLvl = moveset[2][5]
        self.move3name = moveset[2][6]
        
        self.move4bp = moveset[3][0]
        self.move4acc = moveset[3][1]
        self.move4pp = moveset[3][2]
        self.move4effect = moveset[3][3]
        self.move4priority = moveset[3][4]
        self.move4learnLvl = moveset[3][5]
        self.move4name = moveset[3][6]
        # print(moveset[1])
        # self.move1 = moveset[0]
        # self.move2 = moveset[1]
        # self.move3 = moveset[2]
        # self.move4 = moveset[3]

    def replaceMove(self, moveToReplace):
        # user picks move to replace, move position is assigned to moveSelected, cancel button = 0
        moveSelected = 5
        if moveSelected == 0:
            moveSelected #do the update thingy to resume to game
        elif moveSelected == 1:
            self.move1 = moveToReplace
        elif moveSelected == 2:
            self.move2 = moveToReplace
        elif moveSelected == 3:
            self.move3 = moveToReplace
        elif moveSelected == 4:
            self.move4 = moveToReplace

def findLevel(expTot):
    level =  0
    level = expTot // 1000
    return (level + 1)

# class Move:
#     def __init__(self, moveDetails):
#         self.bp = moveDetails[0]
#         self.acc = moveDetails[1]
#         self.pp = moveDetails[2]
#         self.effect = moveDetails[3]
#         self.priority = moveDetails[4]
#         self.learnLvl = moveDetails[5]

lebronStats = [85, 75, 60, 70]
obamaStats = [45, 120, 120, 25]
luffyStats = [50, 90, 90, 60]
ohmStats = [100, 100, 100, 100]
emStats = [70, 100, 50, 20]
bruceStats = [90, 45, 45, 110]
jackStats = [110, 50, 40, 70]
sharkStats = [100, 30, 60, 70]
bearStats = [40, 140, 80, 40]
gruntStats = [40, 40, 40, 40]

# lebronMoves = {
#     "Chasedown Block": Move([0, 100, 10, 1, 1, 0]),
#     "Yabadabadoo Old Navy": Move([0, 50, 20, 2, 0, 0]),
#     "Cleveland!! This is for You!": Move([0, 100, 15, 3, 0, 0]),
#     "Tomohawk Dunk": Move([100, 90, 10, 4, 0, 0])
# }

# lebronMoves = {
#     [[0, 100, 10, 1, 1, 0, "Chasedown Block"],
#     [0, 50, 20, 2, 0, 0, "Yabadabadoo Old Navy"],
#     [0, 100, 15, 3, 0, 0, "Cleveland!! This is for You!"],
#     [100, 90, 10, 4, 0, 0, "Tomohawk Dunk"]]
# }



"""
Effects list (to implement later)
1 - The user runs with high speeds and blocks the enemies attack, this move has priority. If this move is repeated consecutively, its accuracy is halved. 
2 - The user sings with such confidence putting the opponent in a dream-like state causing them to fall asleep.
3 - Increases attack stat by 1 stage - maxes out at 6
4 - This move has a 20% chance of lowering the opponents defense by 1 stage. 
"""

def speedCalc(fighter1, fighter2, movef1, movef2):
    if (movef1.priority == movef2.priority):
        if (fighter1.spd > fighter2.spd):
            return True
        elif (fighter1.spd == fighter2.spd):
            speedTie = random.randint(1,2)
            if speedTie == 1:
                return True
            elif speedTie == 2:
                return False
        elif (fighter1.spd < fighter2.spd):
            return False
    elif (movef1.priority > movef2.priority):
        return True
    elif (movef1.priority < movef2.priority):
        return False
    
def damageCalc(attacker, target, move):
    rng = random.randint(1,100)
    if rng > 95:
        criticalHit = 1.5
    else:
        criticalHit = 1
    damage = (((2 * attacker.level) / 5) * move.bp * (attacker.tempAtk / target.tempDef)) * criticalHit / 50 + 2
    print(damage)
    target.tempHP -= damage
    #if target.tempHP < 0:
        # call method for ending battle loop