import random

choices = ["Rock", "Paper", "Scissors"]

print("Lets play Rock Paper Scissors")

userChoice = input("Do you want Rock, Paper, or Scissors?\n").lower().title()
computerChoice = random.choice(choices)

if computerChoice == userChoice:
    print(f"You both chose {userChoice}, so it's a tie!")
# Computer Rock, Person Scissors
elif computerChoice == choices[0]:
    if userChoice == choices[2]:
        print(f"You chose {userChoice} and the computer chose {computerChoice} so the computer wins this one!")
    else:
        print(f"You chose {userChoice} and the computer chose {computerChoice} so you win this one!")
elif computerChoice == choices[1]:
    if userChoice == choices[0]:
        print(f"You chose {userChoice} and the computer chose {computerChoice} so the computer wins this one!")
    else:
        print(f"You chose {userChoice} and the computer chose {computerChoice} so you win this one!")
elif computerChoice == choices[2]:
    if userChoice == choices[1]:
        print(f"You chose {userChoice} and the computer chose {computerChoice} so the computer wins this one!")
    else:
        print(f"You chose {userChoice} and the computer chose {computerChoice} so you win this one!")