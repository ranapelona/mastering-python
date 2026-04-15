guest_list = ["grandma", "grandpa", "aunt"]
print("Grandma can't make it.")
guest_list[0] = "uncle"

print(f"\nI'm glad {guest_list[1].title()} is still able to make it.".title())
print(f"Even though grandma can't make it  my {guest_list[0].title()} will cover for her.".title())
print(f"My {guest_list[-1].title()} will make it to the party.".title())