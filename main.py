# main.py

from story import introduction, explore_mansion
from characters import NPC, interact_with_npc
from inventory import Inventory, add_item
from puzzles import solve_puzzle

def main():
    character_name = input("Enter your character's name: ")
    print(f"Welcome, {character_name}, to the mysterious mansion investigation!")

    trait = input("Choose a trait (brave, curious, cautious): ").lower()
    skill = input("Choose a special skill (lockpicking, hacking, persuasion): ").lower()
    inventory = Inventory()

    # Introduce the story and setting
    introduction(character_name)
    explore_mansion(character_name, trait, skill, inventory)

    # End game with different endings based on choices
    if "mysterious artifact" in inventory.items:
        print(f"Ending: {character_name}, you uncover the mansion's secret and escape with the artifact!")
    else:
        print(f"Ending: {character_name}, you leave the mansion, the mysteries unsolved.")

if __name__ == "__main__":
    main()
