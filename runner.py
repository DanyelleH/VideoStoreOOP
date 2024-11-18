from classes.Blockbuster import VideoStore
from classes.Inventory import Movie
from classes.Customer import Customer

#Creating the store provides user with available functions.
store = VideoStore()
running = True
while running:
    print("""
    1. View store video inventory
    2. View store customers
    3. View customer rented videos
    4. Add new customer
    5. Rent video
    6. Return video
    7. Exit """)
    choice = input("Select a menu Option: ")
    if choice == "1":
        print("Viewing invetory")
        store.view_invetory()
    if choice == "2":
        print("Viewing all customers")
        store.view_all_customers()
    if choice == "3":
        print("Customers current rentals")
        store.current_rentals()
    if choice == "4":
        print("We have a new customer! ")
        store.new_customer()
    if choice == "5":
        print("Renting video to customer")
        store.rent_video()
    if choice == "6":
        print(" Customers returning video ")
        store.return_video()
    if choice == "7":
        print("Goodbye!...")
        break
    