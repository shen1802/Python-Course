invitees = ["Adam", "James", "Jane"]
print(f"Dear {invitees[0].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[1].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[2].title()}, I would like to invite you to the dinner.")
print(f"{invitees[2].title()} cannot make it to the dinner.")
invitees[2] = "Joshua"
print(f"Dear {invitees[0].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[1].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[2].title()}, I would like to invite you to the dinner.")
