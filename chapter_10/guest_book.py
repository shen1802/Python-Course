from pathlib import Path

names = ''
value = True

print("Type 'end' to finish")
while value:
    name = input("What is your name? ")
    if name.lower() == 'end':
        value = False
    else:
        names += name + '\n'

path = Path("guest_book.txt")
path.write_text(names)
