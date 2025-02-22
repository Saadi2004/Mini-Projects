import random
import string
                       ## FUNCTION FOR CODING INFO ##
def message_to_code():
    message = input("Enter message : ")
    b_message = message.split(" ")
    code = ""
    for word in b_message:
        if len(word) >= 3:
            incomplete_word = word[1:] + word[0]
            r1 = ''.join(random.choices(string.ascii_lowercase, k=3))
            r2 = ''.join(random.choices(string.ascii_lowercase, k=3))
            new_word = r1 + incomplete_word + r2 +" "
            code += new_word
        elif len(word) == 2:
            code += word[::-1] + " "
        else:
            code += word + " "
    print(code)

                         ## FUNCTION FOR DECODING INFORMATION ##
def code_to_message():
    code = input("Enter codes message : ")
    b_code = code.split(" ")
    message = ""
    for word in b_code:
        if len(word) >= 3:
            new_word = word[-4] + word[3:len(word)-4] + " "
            message += new_word
        elif len(word) == 2:
            message += word[::-1] + " "
        else:
            message += word + " "
    print(message)
        
         
                         ## DISPLAY ##
users = {
    "Saad" : "123",
    "Talha": "456",
    "Ahmad": "789"
} 
print("\n-->'Only reistered users can use this system So'<--")
print("-->'Enter your name and password before using this System'<--\n")
name = input("Enter name : ")
password = input("Enter password : ")
name = name.capitalize()

if name in users and users[name] == password:
    print("\n----- Welcome to Code Decode System ----- ")
    
    while True:
        try:
            print("\n0.  Exit")
            print("1.  Code")
            print("2.  Decode")
            choice =int(input("Enter your choice 0, 1 or 2: "))
            if choice == 0:
                print(f"By {name}, Have a Good day")
                break
            elif choice == 1:
                message_to_code()
                
            elif choice == 2:
                code_to_message()
                break
            else:
                print("invalid input")
        except:
            print("Invalid Input")
elif name in users and users[name] != password:
    print("Password is Incorrect")
else:
    print("You are not registered user")
 

