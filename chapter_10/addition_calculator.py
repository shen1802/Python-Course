
active = True
print("Enter [q] to quit")
num_1 = input("Introduce the first number: ")
num_2 = input("Introduce the second number: ")
while active:
    try:
        if num_1 == 'q':
            active = False
            break
        if num_2 == 'q':
            active = False
            break
        sum = int(num_1) + int(num_2)
    except ValueError:
        print("One of the input is not a number!")
    else:
        print(sum)
    num_1 = input("Introduce the first number: ")
    num_2 = input("Introduce the second number: ")
