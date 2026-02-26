from random import randint

class Dice():
    def __init__(self,sides=6):
        self.sides=sides

    def roll_dice(self):
        return randint(1,self.sides)


dice=Dice(21);
result=dice.roll_dice()
print(result)