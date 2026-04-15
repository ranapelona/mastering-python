my_foods = ["pizza", "falafel", "carrot cake"]

friend_foods = my_foods[:]

my_foods.append("Cannoli")

friend_foods.append("Ice cream")

print("My favorite food is:")
for food in my_foods:
    print(f"{food.title()}")

print("\nMy friends favorite food is:")
for friend_food in friend_foods:
    print(f"{friend_food.title()}")