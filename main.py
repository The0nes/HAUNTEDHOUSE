import random


def monster():
    num = random.randrange(1, 100)
    if num <= 30:
        print("A vampire appears.")
    elif num <= 50:
        print("A mummy appears.")
    else:
        print("The room is quiet.")

room = 1
print("You wake up in a dark room")
while True:
    if room == 1:
        print("You are in room 1. You can go 'n' or 'e'.")
        choice = input()
        if choice == 'e':
            room = 2
        elif choice == 'n':
            room = 4
        else:
            print("That is not an option")
    if room == 2:
        print("You are in room 2. You can go 'n' or 'w'")
        monster()
        choice = input()
        if choice == 'w':
            room = 1
        elif choice == 'n':
            room = 3
        else:
            print("not at option, dummy")
    if room == 3:
        print("You are in room 3. You can go 's' or 'w'.")
        choice = input()
        if choice == 's':
            room = 2
        elif choice == 'w':
            room = 4
        else:
            print("Not an option, stupid.")
    if room == 4:
        print("You are in room 4. You can go 's', 'w', or 'e'.")
        choice = input()
        if choice == 'w':
            room = 5
        elif choice == 'e':
            room = 3
        elif choice == 's':
            room = 1
        else:
            print("Not a option, dummy")
    if room == 5:
        print("You are in room 5. You can go 'e'.")
        monster()
        choice = input()
        if choice == 'e':
            room = 4
        else:
            print("That is not a way to.")
