# characters.py

class NPC:
    def __init__(self, name, personality):
        self.name = name
        self.personality = personality
        self.relationship = 0  # 0 = neutral, positive = good, negative = bad

    def interact(self, choice):
        if choice == "ask":
            print(f"{self.name} shares some clues with you.")
            self.relationship += 1
        elif choice == "distance":
            print(f"{self.name} seems offended by your standoffishness.")
            self.relationship -= 1
        else:
            print("Invalid choice. You lose time thinking.")

def interact_with_npc(npc):
    choice = input(f"Do you want to ask {npc.name} about the mansion or keep your distance? (ask/distance): ").lower()
    npc.interact(choice)
