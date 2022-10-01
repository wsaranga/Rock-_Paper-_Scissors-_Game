import random

Rock_Table      = {"rock": "Tie", "scissors": "Win", "paper": "Loss"}
Scissors_Table  = {"rock": "Loss", "scissors": "Tie", "paper": "Win"}
Paper_Table     = {"rock": "Win", "scissors": "Loss", "paper": "Tie"}
Game_Table      = {"rock":Rock_Table,"scissors":Scissors_Table,"paper": Paper_Table}
For_User        = ["rock", "paper", "scissors"]

def game():
    User_marks = 0
    Computer_Marks = 0
    while True:                                                             # Start Game
        User_input = input("Enter your choice :").lower()                  #Get User Input
        if User_input in For_User: # Input Validation
            print(f"you choos: {User_input}")
            computer = For_User[random.randint(0, 2)]                       #Randamly pic by computer
            print(f"computer Choos: {computer}")
            if Game_Table[User_input][computer] == "Tie":                   # Check in nested Dictionary
                print("Another round..!")
            elif Game_Table[User_input][computer] == "Win":                 # Check in nested Dictionary
                User_marks += 1                                             # Update Marks
                print("You Win..!")
                if(input(f"Your mark: {User_marks} and computer marks: {Computer_Marks}. Do you wish to continue ?(Y/N)").upper()=="N"):
                    if User_marks > Computer_Marks:
                        print("Congadulations you win..!")
                        break
                    else:
                        print("May be Next Time..")
                        break
            elif Game_Table[User_input][computer] == "Loss":                # Check in nested Dictionary
                Computer_Marks +=1                                          # Update Marks
                print("Oh..! You Loss")
                if (input(f"Your mark: {User_marks} and computer marks: {Computer_Marks}. Do you wish to continue ?(Y/N)").upper() == "N"):
                    if User_marks > Computer_Marks:
                        print("Congadulations you win..!")
                        break
                    else:
                        print("May be Next Time..")
                        break
        else:
            print("Invalid Input...!")
            game()
game()