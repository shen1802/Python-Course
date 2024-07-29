pizzas = ["Dominos", "Leone", "PizzaHut"]

for pizza in pizzas:
    print(f"I like {pizza} pizza!")

print("I really love pizza!")
friend_pizzas = pizzas[:]
pizzas.append("Peperoni")
friend_pizzas.append("Margaritha")
print(f"My favourite pizzas are: {pizzas}")
print(f"My friend's favourite pizzas are: {friend_pizzas}")


