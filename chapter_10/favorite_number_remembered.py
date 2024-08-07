import json
from pathlib import Path


path = Path("fav_num.json")

if path.exists():
    contents = path.read_text()
    num = json.loads(contents)
    print(f"I know your favorite number! It's {num}")
else:
    num = input("What is your favorite number? ")
    contents = json.dumps(num)
    path.write_text(contents)
    print("I will remember your favorite number")

