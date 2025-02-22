# Function to load data from file
def load_data():
    try:
        with open('library.txt', 'r') as file:
            data = eval(file.read())  # Use eval to safely load dictionary from file
            return data
    except FileNotFoundError:
        return {
            "books": {
                "book1": "writer1",
                "book2": "writer2",
                "book3": "writer3"
            },
            "borrowed_books": {},
            "st_borrowed_books": {},
            "librarian": {
                "Saad": 000
            },
            "students": {
                "Ahmad": 111,
                "Talha": 222,
                "Fahad": 333
            }
        }

# Function to save data to file
def save_data(data):
    with open('library.txt', 'w') as file:
        file.write(repr(data))  # Use repr to safely write dictionary to file

# Initialize data from file
data = load_data()

books = data["books"]
borrowed_books = data["borrowed_books"]
st_borrowed_books = data["st_borrowed_books"]
librarian = data["librarian"]
students = data["students"]

# Search function
def search():
    search = input("Enter book name : ")
    if search in books:
        print(f"\n{search} written by {books[search]} is available")
    else:
        print(f"\n{search} is unavailable")

# Add book function
def add_book():
    book_name = input("Enter book name : ")
    book_writer = input("Enter book writer name : ")
    books[book_name] = book_writer
    save_data(data)
    print(f"\nThe book '{book_name}' written by '{book_writer}' added to the library.")

# Add student function
def add_student():
    st_name = input("Enter student name : ")
    st_name = st_name.capitalize()
    st_password = int(input(f"Create a password for {st_name} : "))
    students[st_name] = st_password
    save_data(data)
    print(f"\nThe student {st_name} is successfully added to the library.")

# Borrow book function
def borrow():
    book_name = input("Enter book name : ")
    if book_name in books:
        print(f"\n{book_name} written by {books[book_name]} is borrowed by {st_name}")
        borrowed_books[book_name] = books[book_name]
        books.pop(book_name)
        st_borrowed_books[st_name] = book_name
        save_data(data)
    else:
        print(f"\n{book_name} is unavailable")

# Return book function
def Return():
    Return_book_name = input("Enter name of book you want to return : ")
    if Return_book_name in borrowed_books:
        print(f"\nThe book '{Return_book_name}' written by '{borrowed_books[Return_book_name]}' returned to the library by {st_name}")
        books[Return_book_name] = borrowed_books[Return_book_name]
        borrowed_books.pop(Return_book_name)
        st_borrowed_books.pop(st_name)
        save_data(data)
    else:
        print("\nThis book is not borrowed from this library")

# Display and main program
print("Are you a Librarian or Student")
while True:
    try:
        print("0. Exit")
        print("1. Librarian")
        print("2. Student")
        st_lib = int(input("Enter your choice : "))
        
        if st_lib == 0:
            break
        
        elif st_lib == 1:  # Librarian
            lib_name = input("Enter your name : ")
            lib_name = lib_name.capitalize()
            lib_password = int(input("Enter your password : "))
            
            if lib_name in librarian and lib_password == librarian[lib_name]:
                print(f"\n{lib_name} logged in to the library.")
                print("Welcome to library Management system")
                
                while True:
                    print("\nWhat do you want to do:")
                    print("Enter 0. Exit")
                    print("Enter 1. Register a student")
                    print("Enter 2. See registered students")
                    print("Enter 3. See all Books")
                    print("Enter 4. Search Book")
                    print("Enter 5. Add book")
                    print("Enter 6. See all borrowed books")
                    print("Enter 7. Students who borrowed books")
                    
                    try:
                        librarian_choice = int(input("Enter your choice : "))
                        
                        if librarian_choice == 0:
                            break
                        elif librarian_choice == 1:
                            add_student()
                            print("========== ========== ==========")
                        elif librarian_choice == 2:
                            for key, value in students.items():
                                print(f"{key}")
                            print("========== ========== ==========")
                        elif librarian_choice == 3:
                            for key, value in books.items():
                                print(f"{key} written by {value}")
                            print("========== ========== ==========")
                        elif librarian_choice == 4:
                            search()
                            print("========== ========== ==========")
                        elif librarian_choice == 5:
                            add_book()
                            print("========== ========== ==========")
                        elif librarian_choice == 6:
                            if not borrowed_books:
                                print("No books borrowed yet")
                            else:
                                for key, value in borrowed_books.items():
                                    print(f"\n{key} written by {value}")
                                print("========== ========== ==========")
                        elif librarian_choice == 7:
                            if not st_borrowed_books:
                                print("No students have borrowed books yet ")
                            else:
                                for key, value in st_borrowed_books.items():
                                    print(f"{value} taken by {key}")
                                print("========== ========== ==========")
                        else:
                            print("Invalid input")
                            print("========== ========== ==========")
                    
                    except ValueError:
                        print("Invalid input")
                        print("========== ========== ==========")
            
            else:
                print("Invalid name and password")
        
        elif st_lib == 2:  # Student
            st_name = input("Enter your name : ")
            st_name = st_name.capitalize()
            st_password = int(input("Enter your password : "))
            
            if st_name in students and st_password == students[st_name]:
                print(f"\n{st_name} logged in to the library.")
                print("Welcome to library Management system")
                
                while True:
                    print("\nWhat do you want to do:")
                    print("Enter 0. Exit")
                    print("Enter 1. Search Book")
                    print("Enter 2. See all Books")
                    print("Enter 3. Borrow Book")
                    print("Enter 4. See all borrowed books")
                    print("Enter 5. Return a Book")
                    
                    try:
                        st_choice = int(input("Enter your choice : "))
                        
                        if st_choice == 0:
                            break
                        elif st_choice == 1:
                            search()
                            print("========== ========== ==========")
                        elif st_choice == 2:
                            for key, value in books.items():
                                print(f"{key} written by {value}")
                            print("========== ========== ==========")
                        elif st_choice == 3:
                            borrow()
                            print("========== ========== ==========")
                        elif st_choice == 4:
                            if not borrowed_books:
                                print("No books borrowed yet")
                            else:
                                for key, value in borrowed_books.items():
                                    print(f"{key} written by {value}")
                                print("========== ========== ==========")
                        elif st_choice == 5:
                            Return()
                            print("========== ========== ==========")
                        else:
                            print("Invalid input")
                            print("========== ========== ==========")
                    
                    except ValueError:
                        print("Invalid Input")
                        print("========== ========== ==========")
            
            else:
                print("Invalid name and password")
        
        else:
            print("Invalid Input")
            print("Enter only 1 or 2")
    
    except ValueError:
        print("Invalid input")
