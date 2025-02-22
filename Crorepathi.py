"""
Questions = ["2 + 2 = ?\noptions \n2   3\n4   5"  , "9 X 4 = ?\noptions \n30   36\n29   40" , "9 / 3 = ?\noptions \n2   3\n8   6" , 'How many balls in a single over in cricket: ?\noptions \n2   3\n4   6']
Answers = ["4" , "36" , "3" , "6"]
prize = [1000,10000,100000,"1 crore"]
money = 0
name = input("Enter your name : ")
print("             ---------------Instructions---------------\n\n-> Total 4 Question you have to answer to get the final prize of 1000000$.")
print("If you give any of the Answer wrong , the game will end with no reward")
print("\n            ------------IMPORTANT KEY WORDS------------")
print("\n|--Continue--| -> moving to the next Question and risking your winning prize for the next Question")
print("|--Quit--| -> take the winning prize and leave the game")
print("===============================================================================================================================")
while True:
    start = input(f"\nHello {name} 'Type yes' to start a game :  ")
    start = start.lower()
    if start == "yes":
        for i in range(len(Questions)):
            
            print(f"Question No {1+i} \n{Questions[i]}")
            answer = input("Answer is : ")
            if answer == Answers[i]:
                print("Right Answer")
                money = prize[i]
                print(f"you won {money}$")
                if i == (len(Questions)-1):
                    print(f"Congratulation {name},You have given all the Answers correct.")
                    print("If you want to play again")
                    break
                while True:
                    continue_or_quit =input("Enter 1 to '--Continue--' Enter 0, to '--Quit--' :  ") 
                    if continue_or_quit == "0":
                        print(f"Congratulations{name}, Your have won {money}$")
                        break
                    elif continue_or_quit == "1" :
                        print("Great")
                        break
                    else:
                        print("Invalid Input")
                        print("Please, Enter Valid input")
            else:
                print("Wrong Answer")
                money *=0
                print(f"{name}You have earned nothing " )
                print(f"Your balance is {money}$ ")
                print("Game Ends")
                print("If you want to play again")
                break
    else:
        print("Invalid Input")
        print("Please Enter Valid input")
                
"""                    
            
                           ## Harry method ##

questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ],
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", "None", 4
  ]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"{questions[i][i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")    
                
                
    
    


