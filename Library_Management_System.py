
books = {
    "book1" : "writer1",
    "book2" : "writer2",
    "book3" : "writer3"
}
borrowed_books ={}
st_borrowed_books = {}
librarian ={
    "Saad" : 000
}
students = {
    "Ahmad" : 111,
    "Talha" : 222,
    "Fahad" : 333
}
                        ## SEARCH FUNCTION ##

def search():
    search = input("Enter book name : ")
    if search in books:
        print(f"\n{search} written by {books[search]} is availble")
    else:
        print(f"\n{search} is unavailable")

                      ## ADD BOOKS FUNCTION ##
def add_book():
    book_name = input("Enter book name : ")
    book_writer = input("Enter book writer name : ")
    books.update({book_name : book_writer})
    print(f"\nThe book '{book_name}' written by '{book_writer}' added to the library : ")
                    
                    ## ADD STUDENT ##
def add_student():
    st_name = input("Enter student name : ")
    st_name = st_name.capitalize()
    st_password = int(input(f"Create a password for a {st_name} : "))
    students.update({st_name : st_password})
    print(f"\nThe student {st_name} is successfully  added to the library : ")
    
                     ## BORROW BOOK FUNCTION ##
def borrow():
    book_name = input("Enter book name : ")
    if book_name in books:
        print(f"\n{book_name} written by {books[book_name]} is borrowed by {st_name} ")
        borrowed_books.update({book_name : books[book_name]})
        books.pop(book_name)
        st_borrowed_books.update({st_name : book_name})
    else:
        print(f"\n{book_name} is unavailable")
        
                          ## Return Book ##
def Return():
    Return_book_name = input("Enter name of book, you want to return : ")
    if Return_book_name in borrowed_books:
        print(f"\nThe book '{Return_book_name}' written by '{borrowed_books[Return_book_name]}' returned to the library by {st_name} : ")
        books.update({Return_book_name : borrowed_books[Return_book_name]})
        borrowed_books.pop(Return_book_name)
        st_borrowed_books.pop(st_name)
    else:
        print("\nThis book is not borrowed from this library")

                          # DISPLAY #                         
print("Are you a Librarian or Student")
while True:
    try:
        print("0. Exit")
        print("1. Librarian")
        print("2. Student")
        st_lib = int(input("Enter your choice : "))
        if st_lib == 0:
            break
        elif st_lib == 1:                           # --> Librarian
            lib_name = input("Enter your name : ")
            lib_name = lib_name.capitalize()
            lib_password = int(input("Enter your password : "))
            if lib_name in librarian and lib_password == librarian[lib_name]:
                print(f"\n{lib_name} logged in to the library.")
                print(f"Welcome to library Management system")
                
            while True:
                if lib_name in librarian and lib_password == librarian[lib_name]:
                    print(f"\nwhat you want to do")
                    print("Enter 0.  Exit")
                    print("Enter 1.  Register a student")
                    print("Enter 2.  See registered students")
                    print("Enter 3.  See all Books")
                    print("Enter 4.  Search Book")
                    print("Enter 5.  Add book")
                    print("Enter 6.  See all borrow books")
                    print("Enter 7.  students who borrow books")
                    try:
                        librarian_choice = int(input("Enter your choice : "))
                        if librarian_choice == 0:
                            break
                        elif librarian_choice == 1:
                            add_student()
                            print("========== ========== ==========")
                        elif librarian_choice == 2:
                            for key , values in students.items():
                                print(f"{key}")
                            print("========== ========== ==========")
                        elif librarian_choice == 3:
                            for key , values in books.items():
                                print(f"{key} written by {values}")
                            print("========== ========== ==========")
                        elif librarian_choice == 4:
                            search()
                            print("========== ========== ==========")
                        elif librarian_choice == 5:
                            add_book()
                            print("========== ========== ==========")
                        elif librarian_choice == 6:
                            if borrowed_books == {}:
                                print("No books borrowed yet")
                            else:
                                for key , values in borrowed_books.items():
                                    print(f"\n{key} written by {values}")
                            print("========== ========== ==========")

                        elif librarian_choice == 7:
                            if st_borrowed_books == {}:
                                print("No student borrowed book yet ")
                            else:
                                for key , values in st_borrowed_books.items():
                                    print(f"{values} taken by {key}")
                            print("========== ========== ==========")
                        else:
                            print("invalid input")
                            print("========== ========== ==========")
                    except:
                        print("Invalid input")
                        print("========== ========== ==========")
                else:
                    print("Invalid name and password")
                    break
        elif st_lib == 2:                              # --> Student
            st_name = input("Enter your name : ")
            st_name = st_name.capitalize()
            st_password = int(input("Enter your password : "))
            if st_name in students and st_password == students[st_name]:
                print(f"\n{st_name} logged in to the library.")
                print(f"Welcome to library Management system")
            while True:
                if st_name in students and st_password == students[st_name]:
                    print(f"\nwhat you want to do")
                    print("Enter 0.  Exit")
                    print("Enter 1.  Search Book")
                    print("Enter 2.  See all Books")
                    print("Enter 3.  Borrow Book")
                    print("Enter 4.  See all borrow books")
                    print("Enter 5.  return a Book")
                    try:
                        st_choice = int(input("Enter your choice : "))
                        if st_choice == 0:
                            break
                        elif st_choice == 1:
                            search()
                            print("========== ========== ==========")
                        elif st_choice == 2:
                            for key , values in books.items():
                                print(f"{key} written by {values}")
                            print("========== ========== ==========")    
                        elif st_choice == 3:
                            borrow()
                            print("========== ========== ==========")
                        elif st_choice == 4:
                            for key , values in borrowed_books.items():
                                print(f"{key} written by {values}")
                            print("========== ========== ==========")
                        elif st_choice == 5:
                            Return()
                            print("========== ========== ==========")   
                        else:
                            print("invalid input")
                            print("========== ========== ==========")
                    except:
                        print("Invalid Input")
                        print("========== ========== ==========")
                else:
                    print("Invalid name and password")
                    break   
        else:
            print("invalid Input")
            print("Enter only  1 or 2")
    except:
        print("Invalid input")