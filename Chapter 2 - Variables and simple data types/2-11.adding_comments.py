"""
Choose two of the programs you've written, and add at least one comment to each. If you don't have anything specific to
write because your programs are too simple at this point, just add your name and the current date at the top of each
program file. Then write one sentence describing what the program does.
"""
# Creating a variable message
message = "Hello world!"
# Printing on the console the content of variable message
print(message)

# Creating a variable name
name = "\t   Adam      \n"
# Printing the content of variable name
print(f"Original string: {name}")
# Removing white spaces on the left of name
print(f"Applied lstrip: {name.lstrip()}")
# Removing white spaces on the right of name
print(f"Applied rstrip: {name.rstrip()}")
# Removing white spaces on the both side of name
print(f"Applied strip: {name.strip()}")
