fav_pizzas = ["pepperoni", "Buffalo", "Hawaiian", "veggie"]
friend_pizzas = fav_pizzas[:]

fav_pizzas.append("meat")

friend_pizzas.append("salmon")

for pizza in fav_pizzas:
    print(f"I like {pizza.title()} pizza.")
print(f"\n I love {fav_pizzas[0].title()} pizza.")
print(f"\n i dislike {fav_pizzas[2].title()} pizza.")
print(f"\n {fav_pizzas[1].title()} pizza was a dissapointing pizza to me.")
print(f"\n My favorite pizzas are:{fav_pizzas}".title())
print(f"\n My friends favorite pizzas are:{friend_pizzas}".title())