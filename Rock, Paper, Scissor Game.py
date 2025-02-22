                       ## Rock , Paper , Scissor ##
import random
choices = ["rock" , "paper" ,"scissor"]
name = input("Enter your name : ")
name = name.capitalize()
print(f"Hello! {name} ,-- WELCOME TO ROCK PAPER SCISSOR GAME -- ")

print(f"\nYou want to play now :) ")
while True:
    play = input("Enter 1 to 'Yes' , 0 to 'No' : ")
    if play =="0" or play == "1":
        if play == "0":
            print(f"Bye {name} , Have a nice day.")
            break
        elif play == "1":
            while True:
                user = input("Enter your choice from (R,P or S) : ")
                user = user.lower()
                if user == "r":
                    user = 'rock'
                elif user == "p":
                    user = "paper"
                elif user == "s":
                    user = "scissor"

                if user == "rock" or user == "paper" or user =="scissor":
                    print(f"Your choice is {user}.")
                    computer = random.choice(choices)
                    print(f"Computer choice is : '{computer}'\n")
                    if user == "rock":
                        if computer == "rock":
                            print("     ---'Draw'---" )
                            print(f"\n{name} do you want to play again? :) ")
                            break
                        elif computer == "paper":
                            print(f"---Sorry {name}, 'You lose'--- ")
                            print(f"\n{name} do you want to play again? :) ")
                            break
                        elif computer == "scissor":
                            print(f"---Congrats {name}, 'You Win'--- " )
                            print(f"\n{name} do you want to play again? :) ")
                            break
                    elif user == "paper":
                        if computer == "rock":
                            print(f"---Congrats {name},'You win'--- " )
                            print(f"\n{name} do you want to play again? :) ")
                            break
                        elif computer == "paper":
                            print("    ---'Draw'--- " )
                            print(f"\n{name} do you want to play again? :) ")
                            break
                        elif computer == "scissor":
                            print(f"---Sorry {name}, 'You loose'--- ")
                            print(f"\n{name} do you want to play again? :) ")
                            break
                    elif user == "scissor":
                        if computer == "rock":
                            print(f"---Sorry {name}, 'You loose'--- ")
                            print(f"\n{name} do you want to play again? :) ")
                            break
                        elif computer == "paper":
                            print(f"---Congrats {name},'You win'--- ")
                            print(f"\n{name} do you want to play again? :) ")
                            break
                        elif computer == "scissor":
                            print("     ---'Draw'--- ")
                            print(f"\n{name} do you want to play again? :) ")
                            break
                else:
                    print("Invalid Input , Try Again")  
    else:
        print("invalid input")  



















#                        ## Rock , Paper , Scissor ##
# import random
# choices = ["rock" , "paper" ,"scissor"]
# name = input("Enter your name : ")
# name = name.capitalize()
# print(f"Hello! {name} ,-- WELCOME TO ROCK PAPER SCISSOR GAME -- ")
# print(f"You want to play now :) ")
# while True:
#     play = input("Enter 1 to 'Yes' , 0 to 'No' : ")
#     if play =="0" or play == "1":
#         if play == "0":
#             print(f"Bye {name} , Have a nice day.")
#             break
#         elif play == "1":
#             while True:
#                 print("Enter your choice : ")
#                 print(f"0).{choices[0]}     1).{choices[1]}     2).{choices[2]}")
#                 user = input("Enter you choice :")
#                 user = int(user)
#                 user_choice = choices[user]
#                 print(f"your choice is {user_choice}")
#                 user = str(user)
#                 user = user.lower()
#                 if user == "0" or user == "1" or user =="2":
#                     computer = random.choice(choices)
#                     print(f"Computer choice is : '{computer}'")
#                     if user == "rock":
#                         if computer == choices[0]:
#                             print("Draw")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                         elif computer == choices[1]:
#                             print(f"Sorry {name}, You lose")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                         elif computer == choices[2]:
#                             print(f"Congrats {name}, You Win")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                     elif user == "paper":
#                         if computer == choices[0]:
#                             print(f"Congrats {name},You win")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                         elif computer == choices[1]:
#                             print("Draw")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                         elif computer == choices[2]:
#                             print(f"Sorry {name}, You loose")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                     elif user == "scissor":
#                         if computer == choices[0]:
#                             print(f"Sorry {name}, You loose")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                         elif computer == choices[1]:
#                             print(f"Congrats {name},You win")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                         elif computer == choices[2]:
#                             print("Draw")
#                             print(f"{name} do you want to play again? :) ")
#                             break
#                 else:
#                     print("Invalid Input , Try Again")  
#     else:
#         print("invalid input")  



