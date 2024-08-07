from pathlib import Path

try:
    path_c = Path("cats.txt")
    cats = path_c.read_text()
    path_d = Path("dogs.txt")
    dogs = path_d.read_text()
except FileNotFoundError:
    print("Cannot find the path of one of the files")
else:
    cats = cats.split()
    dogs = dogs.split()
    print(cats)
    print(dogs)
