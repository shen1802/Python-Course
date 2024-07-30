favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'rust',
   'phil': 'python',
    }

people = ['adam', 'jessica', 'john', 'jane', 'jamie', 'jen', 'phil']

for p in people:
    if p in favorite_languages.keys():
        print(f"Thank you {p.title()} for responding.")
    else:
        print("We kindly invite you to take the poll,", p.title())
