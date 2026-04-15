guest_list = ["grandma", "grandpa", "aunt"]
guest_list[0] = "uncle"
print("Grandma won't be able to make it")

print("\nGood news ! a new table has been found !")

guest_list.insert(0, "brother")
guest_list.insert(3, "dad")
guest_list.append("friend")
print(f"\nMy {guest_list[0].title()} will be coming.")
print(f"\n{guest_list[1].title()} will be coming for grandma.")
print(f"\nI'm glad that {guest_list[2].title()} will be coming to the party.")
print(f"\nmy {guest_list[3].title()} always comes to my party !")
print(f"\nI'm unsure if my {guest_list[4].title()} will be coming to the party")
print(f"\nSince i have more space i invited a {guest_list[5].title()} over.")