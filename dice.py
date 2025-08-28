import random 

class Dice:
    def __init__(self, sides): # define sides
        self.sides = sides

    def roll(self):         #define rolls
        return random.randint(1, self.sides)

dice = Dice(6)      #declare sides of dice

for roll in range(100):  #roll 100 times
    print(dice.roll())

print(dice.roll())


dice = Dice(14) #number of sides
for roll in range (100): #rolls
    print(dice.roll())
