from random import randint


class Die:
    """A representation of a die"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Method that prints a random number between 1 and the number of sides the die has"""
        return randint(1, self.sides)


# Make a 10-sided die and a 20-sided die. Roll each die 10 times.
die10 = Die(10)
die10_results = []
for i in range(11):
    die10_results.append(die10.roll_die())

die20 = Die(20)
die20_results = []
for i in range(10):
    die20_results.append(die20.roll_die())

print(die10_results)
print(die20_results)
