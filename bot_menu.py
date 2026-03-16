while True:
  selection = input("Do you want to check G,S or Q ?").lower()
  if selection == "g":
      grade = int(input("Enter Score: "))
      if grade >= 100:
        print("A")
      elif grade >= 80:
       print("B")
      elif grade >= 70:
       print("C")
      elif grade >= 60:
        print("D")
      else:
        print("F")
  elif selection == "s":
    speed = int(input("Enter speed: "))
    if speed > 65:
      print("Ticket issued")
    elif speed >= 60:
     print("Warning! Slow down.")
    elif speed < 15:
     print("Adjust speed accordingly.")
    else:
     print("Safe driving, keep it up!")
  
  elif selection == "q":
    break