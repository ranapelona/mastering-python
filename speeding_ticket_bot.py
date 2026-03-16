while True:
 try:
    speed = int(input("Enter speed: "))
    if speed > 65:
        print("Ticket issued")
    elif speed >= 60:
        print("Warning! Slow down.")
    elif speed < 15:
       print("Adjust speed accordingly.")
    else:
        print("Safe driving, keep it up!")
 except ValueError:
     print("Please enter a valid answer")