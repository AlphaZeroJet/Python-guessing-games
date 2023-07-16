import random
exitChoice = "Nothing"
while exitChoice != "EXIT":
    print("You are breaking in to mount olympus.")
    print("There are 4 doors, pick 1, 2, 3 or 4")
    playerChoice = input("1,  2, 3 or 4.")
    if playerChoice == "1":
        print("You open the door and see a waterfall.")
        print("1)You can try get down with a rope.")
        print("2)You can leave.")
        print("3)You can climb a tree down.")
        waterChoice = input("1, 2 or 3")
        if waterChoice == "1":
            print("The rope breaks and you die.")
            print("Game Over!")
        elif waterChoice == "2":
            print("You leave and survive")
        elif waterChoice == "3":
            print("A gorrila jumps and kills you.")
            print("Game Over")
    elif playerChoice == "2":
            print("You see a throne room.")
            print("1)You can sit on a throne.")
            print("2)You can explore it.")
            print("3)You can go around and leave.")
            print("4)You can steal somthing.")
            throneChoice = input("1, 2, 3 or 4.")
            if throneChoice == "1":
                print("The throne erupts.")
                print("Game over, you die.")
            elif throneChoice == "2":
                print("Zeus sees you and strikes you with his lightning bolt.")
                print("Game over, you die.")
            elif throneChoice == "3":
                print("You go around and escape.")
            elif throneChoice == "4":
                print("Hades spots you and sends you to the pits of tatarus.")
                print("Game over")
    elif playerChoice == "3":
        print("You see a room with treasure.")
        print("1)You can go around a dragon to get treasure.")
        print("2)You can try to escape.")
        print("3)You can try and fight it.")
        roomChoice = input("1, 2 or 3")
        if roomChoice == "1":
            print("You manage to steal the treasure and you are rich.")
        elif roomChoice == "2":
            print("The dragon spots you and eats you.")
            print("Game over.")
        elif roomChoice == "3":
            print("The dragon breaths fire at you and you are burned to ashes.")
            print("Game over.")
    elif  playerChoice == "4":
        print("You are in a room with a demon.")
        print("You must choose a number between 0, 10.")
        number = int(input("What number do you choose?"))
        rand = random.randint(1,10)
        if number == rand:
            print("You are free.")
            print("You win.")
            print("The demon screams no.")
        else:
            print("The demon tells you that you are its prisoner.")
            print("game over")
            print("you loose")
