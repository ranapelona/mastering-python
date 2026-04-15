import random
big_numbers = list(range(1,1000001))
random.shuffle(big_numbers)
big_numbers.sort()

low_pointer = 0

high_pointer = 999999

target = 777

while low_pointer <= high_pointer:
    middle_index = (low_pointer + high_pointer) // 2
    if big_numbers[middle_index] == target:
        print("Success !")
        break
        
    elif big_numbers[middle_index] < target:
        low_pointer = middle_index +1
    else:
        high_pointer = middle_index -1