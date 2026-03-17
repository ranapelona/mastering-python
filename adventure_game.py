import json
import random
SAVE_FILE = "savegame.json"


def save_game(stats):
    with open(SAVE_FILE, "w") as f:
        json.dump(stats, f)
        print("\n>>> Game saved successfully ! <<<")


def load_game():
    try:
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None


stats = {
    "health": 100,
    "hunger": 50,
    "miles_traveled": 0,
    "bolas": 0,
    "scraps": 0,
    "min_dmg": 5,
    "max_dmg": 15,
    "weapon_lvl": 1
}
if __name__ == "__main__":
    print("--- CURSED DESERT ADVENTURE ---")
    choice = input(
        "Do you want to [Load] a saved game or start [New]? ").lower()
    if choice == "load":
        saved_data = load_game()
        if saved_data:
            stats = saved_data
            print("Welcome back, guy.")
        else:
            print("No save file found. New game started")

    while True:

        h_bar = "█" * max(0, stats["health"] // 10)
        hungr_bar = "█" * max(0, stats["hunger"] // 10)
        print(f"\n" + "="*40)
        print(f"HEALTH: [{h_bar:<10}] {stats['health']}%")
        print(f"HUNGER: [{hungr_bar:<10}] {stats['hunger']}%")
        print(
            f"bolas: {stats['bolas']}  SCRAPS: {stats['scraps']} MILES: {stats['miles_traveled']}")
        print(
            f"Weapon LVL: {stats['weapon_lvl']} (Dmg: {stats['min_dmg']}-{stats['max_dmg']})")
        print("="*40)

        selection = input(
            "You are in a cursed desert. Will you [Rest], [Explore], [Eat], [Scavenge], [Dungeon], [Upgrade], [Save], or [Quit]? ").lower()
        if selection == "save":
            save_game(stats)
            continue

        if selection == "rest":
            stats["health"] = min(100, stats["health"] + 10)
            stats["hunger"] += 2
            print("You had a good nap gained 10 health and got two points hungrier.")

        elif selection == "eat":
            stats["hunger"] = max(0, stats["hunger"] - 8)
            print("You ate a scrumchous burger, your hunger has decreased eight points.")

        elif selection == "dungeon":
            print("\n--- ENTERING THE CURSED CAVE ---")
            confirm = input(
                "It's dangerous inside. Are you sure ? [Yes/No] ").lower()
            if confirm == "yes":
                stats["health"] -= 5
                stats["hunger"] += 10

                event = random.randint(1, 2)
                if event == 1:
                    print(
                        "\n💀 A SKELLY CAME OUT DANCING CUMBIA AND IS READY TO FIGHT !")
                    skelly_hp = 20
                    while skelly_hp > 0 and stats["health"] > 0:
                        print(
                            f">> YOUR HP: {stats['health']}% SKELLY HP: {skelly_hp}")
                        action = input("Do you [Slash] or [Dodge]? ").lower()

                        if action == "slash":
                            damage = random.randint(
                                stats["min_dmg"], stats["max_dmg"])
                            skelly_hp -= damage
                            skelly_hit = random.randint(3, 7)
                            stats["health"] -= skelly_hit
                            print(
                                f"You hit the skelly for {damage}! Skelly hit you for {skelly_hit}!")
                        elif action == "dodge":
                            stats["health"] = min(100, stats["health"] + 2)
                            print(
                                "You danced around his rusty sword and gained 2 HP.")
                        else:
                            print(
                                " You were dazed and confused so the skelly hit you ! -8 HP.")
                            stats["health"] -= 8
                    if stats["health"] > 0:
                        loot = random.randint(10, 30)
                        stats["bolas"] += loot
                        print(
                            f"The skelly has been felled. You found {loot} bolas in his baggie.")

                else:
                    roll = random.randint(1, 4)
                    if roll == 1:
                        found_scraps = random.randint(2, 5)
                        stats["scraps"] += found_scraps
                        print(
                            f"You found a hidden armory ! + {found_scraps} scraps.")
                    elif roll == 2:
                        loot = random.randint(40, 80)
                        stats["bolas"] += loot
                        print(
                            f"You found a golden sarcophagus ! +{loot} bolas.")
                    elif roll == 3:
                        damage = 20
                        stats["health"] -= damage
                        print(f"You triggered a dart trap ! -{damage} Health.")
                        print(f"Your health is now {stats['health']}.")
                    else:
                        print("The cave was empty, but you found a cool rock.")
            else:
                print("You changed your mind")

        elif selection == "scavenge":
            roll = random.randint(1, 3)
            if roll == 1:
                loot = random.randint(5, 15)
                stats["bolas"] += loot
                print(f"You found a lost pouch ! +{loot} bolas")
            elif roll == 2:
                stats["scraps"] += 2
                print("You found some old rusty metal scraps!")
            else:
                stats["health"] -= 10
                print("A scorpion stung you !  -10 Health.")

        elif selection == "upgrade":
            if stats["bolas"] >= 20 and stats["scraps"] >= 2:
                stats["bolas"] -= 20
                stats["scraps"] -= 2
                stats["weapon_lvl"] += 1
                stats["min_dmg"] += 3
                stats["max_dmg"] += 5
                print(
                    f"UPGRADE SUCCESS! Weapon is now level {stats['weapon_lvl']}!")
            else:
                print(
                    "Not enough resources !")

        elif selection == "quit":
            print("Thanks for playing guy.")
            break

        elif selection == "explore":
            stats["miles_traveled"] += 10
            stats["health"] -= 2
            stats["hunger"] += 5
            print(
                f"You run forward. Total distance: {stats['miles_traveled']} miles.")

            if stats["miles_traveled"] == 10:
                print("\n!!! JORGE EL TERRIBLE HAS RISEN FROM UNDER THE SAND !!!")
                jorge_hp = 30
                while jorge_hp > 0 and stats["health"] > 0:
                    h_bar = "█" * min(10, stats["health"] // 10)
                    print(
                        f"\n>> YOUR HP: [{h_bar:<10}] {stats['health']}%  JORGE HP: {jorge_hp}")

                    fight = input("Do you [Slash] or [Dodge]?").lower()

                    if fight == "slash":
                        damage = random.randint(
                            stats["min_dmg"], stats["max_dmg"])
                        jorge_hp -= damage
                        boss_hit = random.randint(5, 10)
                        stats["health"] -= boss_hit
                        print(
                            f"You hit Georgie for {damage}! He hit you back for {boss_hit}!")
                    elif fight == "dodge":
                        stats["health"] = min(100, stats["health"] + 2)
                        print(
                            "You dodged Jorge's fangs! You took 0 damage and gained 2 points.")
                    else:
                        print("You stood confused! Jorge gets a free hit.")
                        stats["health"] -= 10
                if stats["health"] > 0:
                    print(
                        "You have defeated Jorge El Terrible! (Tip: You might want to save now!)")

            elif stats["miles_traveled"] == 20:
                print("\n!!! YOU HAVE REACHED THE PYRAMID. THE MUMMY IS HERE !!!")
                print("He holds Rosalina inside his sarcophagus")
                mummy_hp = 60
                while mummy_hp > 0 and stats["health"] > 0:
                    h_bar = "█" * min(10, stats["health"] // 10)

                    print(
                        f"\n>>  YOUR HP: [{h_bar:<10}] {stats['health']}% MUMMY HP: {mummy_hp}")

                    attack = input(
                        "The mummy has cursed you ! [Attack] or [Dodge]? ").lower()

                    if attack == "attack":
                        damage = random.randint(
                            stats["min_dmg"], stats["max_dmg"])
                        mummy_hp -= damage
                        boss_hit = random.randint(5, 10)
                        stats["health"] -= boss_hit
                        print(
                            f"You hit the Mummy for {damage} damage! He hit you back for {boss_hit}")
                    elif attack == "dodge":
                        stats["health"] = min(100, stats["health"] + 2)
                        print(
                            "You have dodged the Mummy's hit ! You took 0 damage and gained 2 health points.")
                    else:
                        print("The curse is wearing you out, you take damage!")
                        stats["health"] -= 15
                if stats["health"] > 0:
                    print(
                        "The Mummy's soul explodes and lets out a big roar ! The curse has been lifted !")
                    print("You rescue Rosalina. YOU WIN")
                    break
        else:
            print("I don't understand that action.")

        if stats["health"] <= 0:
            print("You Died, Game over.")
            break

        if stats["hunger"] >= 100:
            print("You have starved to death, Game over.")
            break
