print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')
decision = input("Left or right? ")

if decision.lower() != "left":
    print('''You've fallen into a hole.
The game is over.''')
else:
    print("A pool of deadly sharks looms before you")
    decision = input("swim or wait? ")
    if decision.lower() != "wait":
        print("\nYou've been eaten by alligators.\nThe game is over.")
    else:
        print("\nYou wait for an opening and go accross.\nBefore you lay 3 doors; red, blue, and yellow. You can only go through 1."")
        decision = input("red, yellow, or blue? ")
        
        if decision.lower() == "red":
            print("You burn to death.\nGame over.")
        
        elif decision.lower() == "yellow":
            print("You make it to safety and win!")
        
        elif decision.lower() == "blue":
            print("You get eaten by wild beasts\nGame over.")
        
        else:
            print("Game Over.")