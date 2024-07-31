from random import choice
# Make a tuple containing a series of 10 numbers and 5 letters.
values = (11, 4, 6, 8, 18, 34, 23, 10, 16, 9, 'a', 's', 'y', 'h', 'z')
# Make a tuple called my_ticket.
my_ticket = (18, 's', 'z', 10)

winner = []
counter = 0
# Randomly select 4 numbers or letter from the list.

while winner != list(my_ticket):
    for i in range(4):
        winner.append(choice(values))
    counter += 1

print(counter)


