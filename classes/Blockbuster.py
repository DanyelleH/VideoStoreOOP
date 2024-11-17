from classes.Inventory import Movie
from classes.Customer import Customer
import csv
'''
 - Video Store

        def return_video(video_title, customer_id):
            increment the invetory for the video title, remove the title from the customers rentals.
                    

        def available_movies(self):
            returns title and copies available.   
'''
class VideoStore:
    def __init__(self) -> None:
        self.customers = Customer.all_customers() # Key: Customer id Number  value: Customer object.
        self.inventory = Movie.all_movies()

    def view_invetory(self):
        for item in self.inventory:
            print(f"{item.title} has {item.copies_available} rentals available")
    
    def view_all_customers(self):
        for customer_id, customer in self.customers.items():
            print(f"Customer ID: {customer_id}, First, Last name: {customer.firstName}, {customer.lastName}")
    
    def current_rentals(self, customer_id=input):
        customer_id = input("Enter customer id number: ")
        customer =self.customers.get(customer_id, "Invalid Customer ID")
        print(customer.firstName , customer.current_video_rentals.split("/"))

    def new_customer(self,account_type,first_name,last_name,current_video_rentals =""):
        #Duplicate ID's wont be an issue due to customers remaining in the database, with incrementing ID's.
        #this method immediately writes the new users data to the csv file.
        id =len(self.customers) +1
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/customers.csv", mode='a', newline="") as customers:
            writer = csv.writer(customers)
            writer.writerow([id,account_type,first_name,last_name,current_video_rentals])

        #need to update the list of customers in the store everytime a new user is added.
        self.customers = Customer.all_customers()
        print(f"New customer added: ID={id}, Name={first_name} {last_name}, Account Type={account_type}")

    def rent_video(self,video_title, customer_id):
            customer = self.customers.get(customer_id, "Invalid customer id")
            return customer.id
            # check if the customer has reacher their maximum rentals.
            # if not, add that title to their current rentals, and decrement the numer of copies available in the inventory.
            #     if account type = sx:
            #         if current rentals length > 0:
            #             proceed 
            #         else:
            #             upgrade account or return previous movie.
            #     if account type px:
            #         if current_rentals <3:
            #             proceed
            #         else:
            #             return a movie.