import random
# stats is list with base stats, ordered attack, defense, hp, speed
# moveset is dictionary of Move Class objects
# expTot is total exp earned
class Fighter(stats, moveset, expTot):
    def __init__(self, stats, moveset, expTot):
        self.expTot = expTot
        self.level = findLevel(self.expTot)
        self.atk = (stats[0] // 20 + 1) * self.level
        self.dfs = (stats[1] // 20 + 1) * self.level
        self.spd = (stats[2] // 20 + 1) * self.level
        self.hp = (stats[3] // 20 + 1) * self.level
        self.tempAtk = self.atk
        self.tempDef = self.dfs
        self.tempSpd = self.spd
        self.tempHp = self.hp
        self.move1 = moveset[0]
        self.move2 = moveset[1]
        self.move3 = moveset[2]
        self.move4 = moveset[3]

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

lebronStats = [85, 75, 60, 70]
obamaStats = [45, 120, 120, 25]

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
        return True
    
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
        

