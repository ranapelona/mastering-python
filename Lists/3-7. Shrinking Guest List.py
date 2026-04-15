guest_list = ["grandma", "grandpa", "aunt"]
guest_list[0] = "uncle"
print("Grandma won't be able to make it")

print("\nGood news ! a new table has been found !")

guest_list.insert(0, "brother")
guest_list.insert(3, "dad")
guest_list.append("friend")

print("\n Oh no! the tables won't arrive in time ! only two spaces are available.")

kicked_guest = guest_list.pop(1)
print(f"\nSorry for the short notice {kicked_guest.title()} !")

kicked_guest = guest_list.pop(0)
print(f"\nSorry {kicked_guest.title()} it'll have to be next time !")

kicked_guest = guest_list.pop(3)
print(f"\nWe'll have to hang some other time {kicked_guest.title()}.")

kicked_guest = guest_list.pop(2)
print(f"\nSorry {kicked_guest.title()} not enough space !")

print(f"\nDon't worry {guest_list[0].title()} you're still invited.")

print(f"\nYou too {guest_list[1].title()} you're still invited !")


del guest_list[0]

del guest_list [0]

print(guest_list)