print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have multiple chances to guess the correct number.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)
""")

levels = { 
    "1" : {"Easy": 10}, 
    "2" : {"Medium": 5}, 
    "3" : {"Hard": 3}
}

chances = input("Enter your choice: ")

while chances not in list(levels.keys()):
    print("Please enter a valid input.")
    chances = input("Enter your choice: ")

print(f"Great! You have selected the { list(levels[chances].keys())[0] } level.")
