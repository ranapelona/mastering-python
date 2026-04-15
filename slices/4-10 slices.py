my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
my_foods.append("Cannoli")
friend_foods.append("Ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print(f"The first three items in the list are:{my_foods [:3]}")
print(f"\nThree items from the middle of the list are:{my_foods [1:4]}".title())
print(f"\n The last three items on the list are:{my_foods[1:4]}".title())