num_1 = input("Introduce the first number: ")
num_2 = input("Introduce the second number: ")
try:
    sum = int(num_1) + int(num_2)
except ValueError:
    print("One of the input is not a number!")
else:
    print(sum)
