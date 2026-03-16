import random
health = 100
hunger = 50
miles_traveled = 0
bolas = 0
scraps= 0

min_dmg = 5
max_dmg = 15
weapon_lvl = 1

while True:
    
    h_bar = "█" * (health//10)
    hungr_bar = "█" * (hunger//10)
    print(f"\n" + "="*40)
    print(f"HEALTH: [{h_bar:<10}] {health}%")
    print(f"HUNGER: [{hungr_bar:<10}] {hunger}%")
    print(f"bolas: {bolas}  SCRAPS: {scraps} MILES: {miles_traveled}")
    print(f"Weapon LVL: {weapon_lvl} (Dmg: {min_dmg}-{max_dmg})")
    print("="*40)
    
    selection = input("You are in a cursed desert. Will you [Rest], [Explore], [Eat], [Scavenge], [Upgrade], or [Quit]? ").lower()

    if selection == "rest":
        health = min(100, health +10)
        hunger = hunger + 2
        print("You had a good nap gained 10 health and got two points hungrier.")


    elif selection == "eat":
        hunger = max(0,hunger - 8)
        print("You ate a scrumchous burger, your hunger has decreased eight points.")


    elif selection == "scavenge":
        roll = random.randint(1, 3)
        if roll == 1:
            found_bolas = random.randint(5, 15)
            bolas = bolas + found_bolas
            print(f"You found a lost pouch ! +{found_bolas} bolas")
        elif roll == 2:
            scraps = scraps + 1
            print("You found some old rusty metal scraps!")
        else:
            health = health - 10
            print("A scorpion stung you !  -10 Health.")
    
    elif selection == "upgrade":
        if bolas >= 20 and scraps >= 2:
            bolas = bolas - 20
            scraps = scraps - 2
            weapon_lvl = weapon_lvl +1
            min_dmg = min_dmg + 3
            max_dmg = max_dmg + 5
            print(f"UPGRADE SUCCESS! Weapon is now level {weapon_lvl}!")
        else: print(f"Not enough resources ! Need 20 bolas & 2 scraps. You have: {bolas}B, {scraps}S)")
    
    elif selection == "quit":
        print("Thanks for playing guy.")
        break
    
    elif selection == "explore":
          miles_traveled = miles_traveled + 10
          health = health - 2
          hunger = hunger + 5
          print(f"You run forward. Total distance: {miles_traveled} miles.")

          if miles_traveled == 10:
             print("\n!!! JORGE EL TERRIBLE HAS RISEN FROM UNDER THE SAND !!!")
             jorge_hp = 30
             while jorge_hp > 0 and health > 0:
              h_bar = "█" * min(10, health // 10)
              
              print(f"\n>> YOUR HP: [{h_bar:<10}] {health}%  JORGE HP: {jorge_hp}")

              fight = input("Do you [Slash] or [Dodge]").lower()
                
              if fight == "slash":
                damage = random.randint(min_dmg, max_dmg)
                jorge_hp -= damage
                boss_hit = random.randint(5, 10)
                health -= boss_hit
                print(f"You hit Georgie for {damage}! He hit you back for {boss_hit}!")
              elif fight == "dodge":
                  health = health + 2
                  print("You dodged Jorge's fangs! You took 0 damage and gained 2 points.")
              else:
                    print("You stood confused! Jorge gets a free hit.")
                    health -= 10
             if health > 0:
                print("You have defeated Jorge El Terrible! Continue your journey.")

        
        
          elif miles_traveled == 20:
            print("\n!!! YOU HAVE REACHED THE PYRAMID. THE MUMMY IS HERE !!!")
            print("He holds Rosalina inside his sarcophagus")
            mummy_hp = 60
            while mummy_hp > 0 and health > 0:
                h_bar ="█" * min(10, health // 10)
                
                print(f"\n>>  YOUR HP: [{h_bar:<10}] {health}% MUMMY HP: {mummy_hp}")
                
                attack = input("The mummy has cursed you ! [Attack] or [Dodge]? ").lower()
                
                if attack == "attack":
                    damage = random.randint(min_dmg, max_dmg)
                    mummy_hp -= damage
                    boss_hit = random.randint(5, 10)
                    health -= boss_hit
                    print(f"You hit the Mummy for {damage} damage! He hit you back for {boss_hit}")
                elif attack == "dodge":
                    health = health + 2
                    print("You have dodged the Mummy's hit ! You took 0 damage and gained 2 health points.")
                else:
                    print("The curse is wearing you out, you take damage!")
                    health -= 15
            if health > 0:
                    print("The Mummy's soul explodes and lets out a big roar ! The curse has been lifted !")
                    print("You rescue Rosalina. YOU WIN")
                    break
    else:
        print("I don't understand that action.") 

    if health <= 0:
           print("You Died, Game over.")
           break
          
    if hunger >= 100:
           print("You have starved to death, Game over.")
           break