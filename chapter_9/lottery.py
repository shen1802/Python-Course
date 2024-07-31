from random import choice
# Make a tuple containing a series of 10 numbers and 5 letters.
values = (11, 4, 6, 8, 18, 34, 23, 10, 16, 9, 'a', 's', 'y', 'h', 'z')

winner = []
# Randomly select 4 numbers or letter from the list.
for i in range(4):
    winner.append(choice(values))

print(f"Any ticket matching these 4 {winner} numbers or letter wins a prize.")

