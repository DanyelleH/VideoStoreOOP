from classes.Inventory import Movie
from classes.Customer import Customer
import csv
'''
 - Video Store
    
        def rent_video(video_title, Customer_id):
            check if the customer has reacher their maximum rentals.
            if not, add that title to their current rentals, and decrement the numer of copies available in the inventory.
                if account type = sx:
                    if current rentals length > 0:
                        proceed 
                    else:
                        upgrade account or return previous movie.
                if account type px:
                    if current_rentals <3:
                        proceed
                    else:
                        return a movie.

        def return_video(video_title, customer_id):
            increment the invetory for the video title, remove the title from the customers rentals.
                    

        def available_movies(self):
            returns title and copies available.   
'''
class VideoStore:
    def __init__(self) -> None:
        self.customers = Customer.all_customers()
        self.inventory = Movie.all_movies()

    def view_invetory(self):
        for item in self.inventory:
            print(f"{item.title} has {item.copies_available} rentals available")
    
    def view_all_customers(self):
        for item in self.customers:
            print(f"Customer ID: {item.id} First, Last: {item.firstName}, {item.lastName} ")
    
    def current_rentals(self, customer_id=input):
        customer_id = input(" Enter customer id number: ")
        for item in self.customers:
            if item.id == customer_id:
                return item.current_video_rentals.split("/")
        return "Id not in database"

    def new_customer(self,account_type,first_name,last_name,current_video_rentals =""):
        #Duplicate ID's wont be an issue due to customers remaining in the database, with incrementing ID's.
        id =len(self.customers) +1
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/customers.csv", mode='a', newline="") as customers:
            writer = csv.writer(customers)
            writer.writerow([id,account_type,first_name,last_name,current_video_rentals])