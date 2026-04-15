guest_list = ["grandma", "grandpa", "aunt"]
guest_list[0] = "uncle"
print("Grandma won't be able to make it")

print("\nGood news ! a new table has been found !")

guest_list.insert(0, "brother")
guest_list.insert(3, "dad")
guest_list.append("friend")

print(f"{len(guest_list)} people are joining me on my party.")