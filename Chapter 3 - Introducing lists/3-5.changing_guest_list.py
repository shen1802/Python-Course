"""
You just heard that one of your guests can't make the dinner, so you need to send out a new set of invitations. You'll
have to think of someone else to invite.
* Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the
guest who can't make it.
* Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting.
* Print a second set of invitation messages, one for each person who is still in your list.
"""
invitees = ["Adam", "James", "Jane"]
print(f"Dear {invitees[0].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[1].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[2].title()}, I would like to invite you to the dinner.")
print(f"{invitees[2].title()} cannot make it to the dinner.")
invitees[2] = "Joshua"
print(f"Dear {invitees[0].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[1].title()}, I would like to invite you to the dinner.")
print(f"Dear {invitees[2].title()}, I would like to invite you to the dinner.")
