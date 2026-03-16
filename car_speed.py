try:
 car_speed = int(input("Please enter car speed"))
 if car_speed > 65:
  print("Ticket issued")
 elif car_speed > 60 and car_speed <= 65:
  print("Warning!")
 else:
  print("Safe driving")
except ValueError:
 print("Please enter a valid input. ")