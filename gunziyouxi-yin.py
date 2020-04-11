#!/usr/bin/env python3
sticks = 21

print("There are 21 sticks, you can take 1-4 number of sticks at a time.")
print("Whoever will take the last stick will loose")

while True:
    print("Sticks left: " , sticks)
    if sticks == 1:
        print("You took the last stick, you loose")
        break
    sticks_taken = int(input("Take sticks(1-4):"))
    if sticks <= 6:
        if sticks_taken >= sticks :
            print("The computer took the last stick, you win")
            break
    if sticks_taken >= 5 or sticks_taken <= 0:
        print("Wrong choice")
        continue
    print("Computer took: " , (6 - sticks_taken) , "\n")
    sticks -= 6