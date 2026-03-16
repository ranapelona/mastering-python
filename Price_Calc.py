try: 
 items = int(input("How many items? "))
 if items > 10:
  print("You get a discount !")
 else:
   print("Standard price.")
except ValueError:
 print("Please use numbers, not words ! ")
