from pathlib import Path

learning_python = []
path = Path('learning_python.txt')
contents = path.read_text()
lines = contents.splitlines()

for line in lines:
    learning_python.append(line)
    print(line)

[print(line) for line in learning_python]



