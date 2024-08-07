from pathlib import Path
import json

path = Path("person.json")
if path.exists():
    contents = path.read_text()
    person = json.loads(contents)
    print(f"Welcome back, {person['name']}")
else:
    try:
        name = input("What is your name? ")
        age = input("What is your age? ")
        job = input("What is your job? ")
    except ValueError:
        print(f"The age value is not correct {age}")
    else:
        person = {"name": name, "age": int(age), "job": job}
        contents = json.dumps(person)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {person['name']}!")
