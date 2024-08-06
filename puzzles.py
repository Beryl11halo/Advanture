# puzzles.py

def solve_puzzle(puzzle_type):
    if puzzle_type == "riddle":
        print("Solve this riddle: I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?")
        answer = input("Your answer: ").lower()
        if answer == "echo":
            print("Correct! You solved the riddle.")
        else:
            print("Incorrect. The puzzle remains unsolved.")
    elif puzzle_type == "code":
        print("Enter the 4-digit code to unlock the door.")
        code = input("Your code: ")
        if code == "1234":
            print("The door unlocks with a click.")
        else:
            print("Incorrect code. The door remains locked.")
