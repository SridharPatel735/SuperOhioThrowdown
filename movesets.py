
"""class Move:
    def __init__(self, moveDetails):
        self.bp = moveDetails[0]
        self.acc = moveDetails[1]
        self.pp = moveDetails[2]
        self.effect = moveDetails[3]
        self.priority = moveDetails[4]
        self.learnLvl = moveDetails[5]


lebronMoves = {
    "Chasedown Block": Move([0, 100, 10, 1, 1, 0]),
    "Yabadabadoo Old Navy": Move([0, 50, 20, 2, 0, 0]),
    "Cleveland!! This is for You!": Move([0, 100, 15, 3, 0, 0]),
    "Tomohawk Dunk": Move([100, 90, 10, 4, 0, 0])
}

ohmMoves = {
    "Super Ohio Throwdown": Move([150, 100, 1, 5, 0, 0]),
    "AtOHMic BOHMb": Move([20, 100, 10, 6, 0, 0]),
    "Attack of the ClOHMs": Move([0, 50, 5, 7, 0, 0]),
    "OHMazing Grace": Move([0, 100, 3, 8, 0, 0])
}

luffyMoves = {
    "Gatling Punch": Move([10, 100, 5, 9, 0, 0]),
    "Jet Pistol": Move([40, 100, 20, 0, 1, 0]),
    "Giant Pistol": Move([150, 100, 5, 5, 0, 0]),
    "Gear Change": Move([0, 100, 5, 10, 0, 0])
}

sharkMoves = {
    "Tidal Wave": Move([0, 100, 10, 11, 0, 0]),
    "Fish Feast": Move([0, 90, 5, 8, 0, 0]),
    "Bite": Move([60, 100, 10, 0, 0, 0]),
    "Puncture Prey": Move([20, 100, 10, 6, 0, 0])
}

grizzlyMoves = {
    "Bite": Move([60, 100, 10, 0, 0, 0]),
    "Shake the Tree": Move([0, 100, 10, 12, 0, 0]),
    "Bear Down": Move([0, 100, 1, 13, 0, 0]),
    "Berry Bush Beatdown": Move([30, 100, 10, 14, 0, 0]),
    "Unbearable Bunker": Move([0, 100, 1, 15, 0, 15])
}

bruceMoves = {
    "Leg Sweep": Move([30, 100, 10, 0, 0, 0]),
    "One Inch Punch": Move([10, 100, 3, 12, 0, 0]),
    "Lop Sao Backfist": Move([15, 100, 10, 0, 1, 0]),
    "Block": Move([0, 100, 10, 1, 1, 0]),
    "Lightning Fast Punches": Move([7, 100, 5, 9, 0, 15])
}

eminemMoves = {
    "Killshot": Move([140, 100, 1, 0, 0, 15]),
    "Rap God": Move([20, 100, 10, 11, 0, 0]),
    "Not Afraid": Move([0, 100, 1, 13, 0, 0]),
    "8 Mile Melee": Move([10, 100, 5, 9, 0, 0]),
    "Till I Collapse": Move([0, 100, 1, 13, 0, 0]),
    "Music to Be Murdered By": Move([0, 50, 20, 2, 0, 10]) 
}

obamaMoves = {
    "Let Me Be Clear": Move([0, 100, 3, 7, 0, 0]),
    "Campaign Trail Stomp": Move([20, 100, 5, 17, 0, 0]),
    "Landslide Victory": Move([0, 100, 5, 16, 0, 0]),
    "Endorsement Enforcement": Move([30, 100, 10, 14, 0, 0])
}

sparrowMoves = {
    "Drunken Dodge": Move([0, 100, 5, 1, 0, 0]),
    "Crash the Boat": Move([90, 100, 3, 18, 0, 0]),
    "Slash and Dash": Move([40, 100, 5, 11, 0, 0]),
    "Pillage": Move([0, 100, 1, 19, 0, 0])
}

gruntMoves = {
    "Shout": Move([30, 100, 5, 4, 0, 0]),
    "Punch": Move([50, 100, 10, 0, 0, 0]),
    "Get Angry": Move([0, 100, 3, 3, 0, 0]),
    "Stop Right There": Move([0, 100, 5, 16, 0, 0])
}

Effects list (to implement later)
1 - The user runs with high speeds and blocks the enemies attack, this move has priority. If this move is repeated consecutively, its accuracy is halved. 
2 - The user sings with such confidence putting the opponent in a dream-like state causing them to fall asleep.
3 - Increases attack stat by 1 stage - maxes out at 6
4 - This move has a 20% chance of lowering the opponents defense by 1 stage. 
5 - T1 charge up (no damage), T2 attack 
6 - Ohm uses his toxic voice chat energy to irradiate the battle. Opponent takes 1/16th chip damage per turn for the next 5 turns
7 - Decreases opponent accuracy by 1/8th if it hits
8 - heals 50% health
9 - hits 4-10 times
10 - Switch attack and defense stats
11 - increases speed stat by 1 stage - maxes out at 6
12 - drops opponent defense stat by 1 stage - maxes out at 6
13 - only works if user is under 25% hp. drops defense by 50%, increases attack and speed by 100%
14 - heals 25% of damage dealt
15 - increases defense stat by 1 stage - maxes out at 6
16 - drops opponent speed by 1 stage - maxes
17 - increases attack 10% each time the move is used
18 - deals 33% damage of attack to user
19 - turns the user's defense stat into the enemy's defense stat
"""
lebronMoves = [[0, 100, 10, 1, 1, 0, "Chasedown Block"],
    [0, 50, 20, 2, 0, 0, "Yabadabadoo Old Navy"],
    [0, 100, 15, 3, 0, 0, "Cleveland!! This is for You!"],
    [80, 75, 10, 4, 0, 0, "Tomohawk Dunk"]]

ohmMoves = [[150, 100, 1, 5, 0, 0, "Super Ohio Throwdown"],
    [20, 100, 10, 6, 0, 0, "AtOHMic BOHMb"],
    [0, 50, 5, 7, 0, 0, "Attack of the ClOHMs"],
    [0, 100, 3, 8, 0, 0, "OHMazing Grace"]]

luffyMoves = [[10, 100, 5, 9, 0, 0, "Gatling Punch"],
    [40, 100, 20, 0, 1, 0, "Jet Pistol"],
    [150, 100, 5, 5, 0, 0, "Giant Pistol"],
    [0, 100, 5, 10, 0, 0, "Gear Change"]]

sharkMoves = [[0, 100, 10, 11, 0, 0, "Tidal Wave"],
    [0, 90, 5, 8, 0, 0, "Fish Feast"],
    [60, 100, 10, 0, 0, 0, "Bite"],
    [20, 100, 10, 6, 0, 0, "Puncture Prey"]]

grizzlyMoves = [[60, 100, 10, 0, 0, 0, "Bite"],
    [0, 100, 10, 12, 0, 0, "Shake the Tree"],
    [0, 100, 1, 13, 0, 0, "Bear Down"],
    [30, 100, 10, 14, 0, 0, "Berry Bush Beatdown"],
    [0, 100, 1, 15, 0, 15, "Unbearable Bunker"]]

bruceMoves = [[30, 100, 10, 0, 0, 0, "Leg Sweep"],
    [10, 100, 3, 12, 0, 0, "One Inch Punch"],
    [15, 100, 10, 0, 1, 0, "Lop Sao Backfist"],
    [0, 100, 10, 1, 1, 0, "Block"],
    [7, 100, 5, 9, 0, 15, "Lightning Fast Punches"]]

eminemMoves = [[140, 100, 1, 0, 0, 15, "Killshot"],
    [20, 100, 10, 11, 0, 0, "Rap God"],
    [0, 100, 1, 13, 0, 0, "Not Afraid"],
    [10, 100, 5, 9, 0, 0, "8 Mile Melee"],
    [0, 100, 1, 13, 0, 0, "Till I Collapse"],
    [0, 50, 20, 2, 0, 10, "Music to Be Murdered By"]]

obamaMoves = [[0, 100, 3, 7, 0, 0, "Let Me Be Clear"],
    [20, 100, 5, 17, 0, 0, "Campaign Trail Stomp"],
    [0, 100, 5, 16, 0, 0, "Landslide Victory"],
    [30, 100, 10, 14, 0, 0, "Endorsement Enforcement"]]

sparrowMoves = [[0, 100, 5, 1, 0, 0, "Drunken Dodge"],
    [90, 100, 3, 18, 0, 0, "Crash the Boat"],
    [40, 100, 5, 11, 0, 0, "Slash and Dash"],
    [0, 100, 1, 19, 0, 0, "Pillage"]]

gruntMoves = [[30, 100, 5, 4, 0, 0, "Shout"],
    [50, 100, 10, 0, 0, 0, "Punch"],
    [0, 100, 3, 3, 0, 0, "Get Angry"],
    [0, 100, 5, 16, 0, 0, "Stop Right There"]]