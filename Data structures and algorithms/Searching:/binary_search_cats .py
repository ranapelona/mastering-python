cat_shelter = list(range(0,100))
low = 0
high = 99
target = 100
while low <= high:
    mid = low + (high - low) //2
    if cat_shelter[mid] == target:
        print("Congrats you found the kitty !")
        break
    elif cat_shelter[mid] < target:
        low = mid +1
    else:
        high = mid -1
if low > high:
        print("Couldn't find the kitty :(")

