import json
from pathlib import Path

num = input("What is your favorite number? ")
path = Path("fav_num.json")
contents = json.dumps(num)
path.write_text(contents)

path = Path("fav_num.json")
contents = path.read_text()
num = json.loads(contents)
print(f"I know your favorite number! It's {num}")
