rivers = {'egipt': 'nile', 'brazil': 'amazon', 'spain': 'ebro'}

for k, v in rivers.items():
    print(f"The {v.title()} runs through {k.title()}.")

[print(k.title()) for k in rivers.keys()]
[print(v.title()) for v in rivers.values()]
