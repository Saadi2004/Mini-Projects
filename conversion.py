

                    ## FUNCTION FOR BINARY CONVERSION TO DECIMAL  ##
def binary_conversion():   
    while True:                    
        binary = input("Enter a Binary number : ")
        decimal = 0
        j = 0
        for i in range(len(binary)-1, -1 , -1):
            int_binary =  int(binary[i])
            if int_binary > 1:
                print("Invalid input")
                break
            else:    
                decimal = decimal + (int_binary * (2**j))     
                j = j+1
        if decimal==0:
            quit
        else:
            print(decimal)
            break
                    ## FUNCTION FOR DECIMAL CONVERSION TO BINARY  ##

def decimal_converter():
    while True:
        try:
            decimal = int(input("Enter a Decimal number : "))
            binary = ''
            if decimal > 1:
                while decimal > 1:
                    remain = decimal%2
                    decimal = decimal//2
                    str_remain = str(remain)
                    binary += str_remain
                if decimal ==1:
                        binary += '1'    
                print(binary[::-1]) 
                break
        except:
            print("invalid input")

                  ## DISPLAY ##
print("----- Welcome to Conversion Calculator -----\n")
# print("1. Binary to Decimal")
# print("2. Decimal to Binary")

while True:
    try:
        print("\n1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Exit")
        choice = int(input("\nEnter your choice : "))
        if choice == 1 or choice == 2 or choice == 3:
            if choice == 1:
                binary_conversion()
                break
            elif choice == 2:
                decimal_converter() 
                break
            elif choice == 3:
                break
        else:
            print("invalid input ")

    except:
        if choice == 1:
            print("Invalid input ")
            binary_conversion()
                
        elif choice == 2:
            print("Invalid input ")
            decimal_converter() 
        
        elif choice == 3:
            print("Invalid input ")
         

                
        
 
        
                              ### Practice ###
                                  
# def binary_conversion():   
#     while True:                    
#         binary = input("Enter a Binary number : ")
#         decimal = 0
#         j = 0
#         for i in range(len(binary)-1, -1 , -1):
#             int_binary =  int(binary[i])
#             if int_binary > 1:
#                 print("Invalid input")
#                 break
#             else:    
#                 decimal = decimal + (int_binary * (2**j))     
#                 j = j+1
#         if decimal==0:
#             quit
#         else:
#             print(decimal)
#         break

    
"""    
def binary_conversion():
    binary = input("Enter a Binary number : ")
    decimal = 0
    j = 0
    for i in range(len(binary)-1, -1 , -1):
        int_binary =  int(binary[i])
        decimal = decimal + (int_binary * (2**j))     
        j = j+1
    print(decimal)
"""
              
                     
                        ## FUNCTION FOR DECIMAL CONVERSION TO BINARY  ##




# def decimal_converter():
#     decimal = int(input("Enter a Decimal number : "))
#     binary = ''
#     if decimal > 1:
#         while decimal > 1:
#             remain = decimal%2
#             decimal = decimal//2
#             str_remain = str(remain)
#             binary += str_remain
#         if decimal ==1:
#             binary += '1'    
#         print(binary[::-1]) 