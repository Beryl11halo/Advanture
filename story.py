# story.py

def introduction(character_name):
    print(f"{character_name}, you have been called to investigate a mysterious mansion.")
    print("The mansion is known for its strange occurrences and supernatural phenomena.")
    print("Your mission is to explore the mansion, find clues, and uncover its secrets.")

def explore_mansion(character_name, trait, skill, inventory):
    print("You arrive at the mansion and notice a strange glow coming from the windows.")
    choice1 = input("Do you want to enter through the front door or explore the garden? (enter/garden): ").lower()

    if choice1 == "enter":
        explore_mansion_inside(character_name, trait, skill, inventory)
    elif choice1 == "garden":
        explore_garden(character_name, trait, skill, inventory)
    else:
        print("Invalid choice. The game ends.")

def explore_mansion_inside(character_name, trait, skill, inventory):
    print("You enter the mansion's grand hall.")
    choice2 = input("Do you want to explore the left wing, right wing, or upstairs? (left/right/upstairs): ").lower()
    
    if choice2 == "left":
        library(character_name, skill, inventory)
    elif choice2 == "right":
        device_room(character_name, skill, inventory)
    elif choice2 == "upstairs":
        eerie_corridor(character_name, trait, skill, inventory)
    else:
        print("Invalid choice. You lose time wandering.")

def explore_garden(character_name, trait, skill, inventory):
    print("You discover a hidden pathway in the garden leading to a secret basement.")
    print("Inside the basement, you find a mysterious altar and strange symbols.")
    # Further story progression in the basement

def library(character_name, skill, inventory):
    print("You find a library with ancient books and a locked safe.")
    if skill == "lockpicking":
        print("Using your lockpicking skill, you open the safe and find a mysterious artifact.")
        add_item(inventory, "mysterious artifact")
    else:
        print("You can't open the safe without the right skill.")

def device_room(character_name, skill, inventory):
    print("You enter a room with a strange device and a console.")
    choice3 = input("Do you want to inspect the device or the console? (device/console): ").lower()
    if choice3 == "device":
        print("The device seems to be some sort of energy generator. It could be dangerous.")
        # Further story progression
    elif choice3 == "console":
        if skill == "hacking":
            print("You hack into the console and reveal hidden files.")
            # Further story progression with files
        else:
            print("You need hacking skills to access the console.")

def eerie_corridor(character_name, trait, skill, inventory):
    print("You find an eerie corridor with locked doors.")
    # Further story progression with locked doors and exploration
