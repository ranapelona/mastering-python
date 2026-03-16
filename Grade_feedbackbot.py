while True:
 try:
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
 except ValueError:
   print("Please enter a valid answer ! ")