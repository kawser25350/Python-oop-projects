class Star_Cinema:
    __hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.__hall_list.append(hall)



class Hall(Star_Cinema):
    def __init__(self, hall_no, rows=5, cols=5):
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_tuple = (id, movie_name, time)
        self.__show_list.append(show_tuple)
        seat_map = [['0' for _ in range(self.__cols)] for _ in range(self.__rows)]
        self.__seats[id] = seat_map

    def book_seats(self, show_id, seats_to_book):
        if show_id not in self.__seats:
            print("Invalid show ID.")
            return
        for row, col in seats_to_book:
            if not (0 <= row < self.__rows and 0 <= col < self.__cols):
                print(f"Invalid seat position: Row {row}, Column {col}")
                continue
            if self.__seats[show_id][row][col] == '1':
                print(f"Seat at Row {row}, Column {col} is already booked.")
            else:
                self.__seats[show_id][row][col] = '1'

    def view_show_list(self):
        if not self.__show_list:
            print("No shows are available.")
            return
        print("List of Shows:")
        for show in self.__show_list:
            print(f"ID: {show[0]}, Movie: {show[1]}, Time: {show[2]}")

    def show_seats_matrix(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID.")
            return
        print(f"Seat Map for Movie ID {show_id}:")
        for row in range(self.__rows):
            row_display = ""
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == '0':
                    row_display += "[ ] "
                else:
                    row_display += "[b] "
            print(row_display)

    def view_available_seats(self, show_id):
        if show_id not in self.__seats:
            print("Invalid show ID.")
            return
        print(f"Seat Map for Movie ID {show_id}:")
        available_seats = []
        for row in range(self.__rows):
            row_display = ""
            for col in range(self.__cols):
                if self.__seats[show_id][row][col] == '0':
                    row_display += "[ ] "
                    available_seats.append(f"Row {row}, Col {col}")
                else:
                    row_display += "[b] "
            print(row_display)

        if available_seats:
            print("\nAvailable Seats:")
            for seat in available_seats:
                print(seat)
        else:
            print("\nNo available seats.")


hall1 = Hall(101)
hall1.entry_show(1, "Avengers: Endgame", "5:00 PM")
hall1.entry_show(2, "Batman Begins", "7:30 PM")

while True:
    print("*********************")
    print("1. Add Movie List")
    print("2. Show All Movies")
    print("3. Book Ticket")
    print("4. Show Available Seats")
    print("5. Exit")
    print("*********************")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue
    print("")

    if choice == 1:
        movie_id = int(input("Enter Movie ID: "))
        movie_name = input("Enter Movie Name: ")
        movie_time = input("Enter Movie Time: ")
        hall1.entry_show(movie_id, movie_name, movie_time)
        print(f"Movie '{movie_name}' added successfully!")
        print("")

    elif choice == 2:
        hall1.view_show_list()
        print("")

    elif choice == 3:
        movie_id = int(input("Enter Movie ID: "))
        if movie_id not in [show[0] for show in hall1._Hall__show_list]:
            print("Invalid Movie ID! Returning to menu.")
            continue
        hall1.show_seats_matrix(movie_id)
        try:
            row = int(input("Enter Row (0-4): "))
            col = int(input("Enter Column (0-4): "))
            if not (0 <= row < hall1._Hall__rows and 0 <= col < hall1._Hall__cols):
                print("Invalid seat position. Row and column must be between 0 and 4.")
                continue
            hall1.book_seats(movie_id, [(row, col)])
        except ValueError:
            print("Invalid input for row or column. Please enter valid integers.")
        print("")

    elif choice == 4:
        movie_id = int(input("Enter Movie ID: "))
        hall1.view_available_seats(movie_id)
        print("")

    elif choice == 5:
        print("Exiting...")
        print("")
        break

    else:
        print("Invalid choice. Please try again.")
        print("")
