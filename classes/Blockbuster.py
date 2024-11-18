from classes.Inventory import Movie
from classes.Customer import Customer
import csv
'''
 - Video Store
        def available_movies(self):
            returns title and copies available.   
'''
class VideoStore:
    def __init__(self) -> None:
        self.customers = Customer.all_customers() # Key: Customer id Number  value: Customer object.
        self.inventory = Movie.all_movies() # Key: Movie Title   Value: Mobie object

    def view_invetory(self):
        for title,movie in self.inventory.items():
            print(f"Movie Title: {title} has {movie.copies_available} rentals available")
    
    def view_all_customers(self):
        for customer_id, customer in self.customers.items():
            print(f"Customer ID: {customer_id}, First, Last name: {customer.firstName}, {customer.lastName}")
    
    def current_rentals(self, customer_id=input):
        customer_id = input("Enter customer id number: ")
        customer =self.customers.get(customer_id, "Invalid Customer ID")
        print(customer.firstName , customer.current_video_rentals)

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
            customer_id = str(customer_id)
            customer = self.customers[customer_id]
            current_rentals = (customer.current_video_rentals.split("/"))
            if customer.account_type == "Sx":
                if len(current_rentals) == 1:
                    # handles cases where the user has no rentals in their name
                    if current_rentals[0] == "":
                        customer.current_video_rentals = customer.current_video_rentals + "/" + video_title
                        '''
                       #### implement method to check if the video is in the invetory, 
                        as well as ability to update inventory ####
                        # Implement method to update the csv file.
                        '''
                        return f"{customer.firstName} is now renting {video_title}"
                else: 
                    print(f"Return {customer.current_video_rentals} before renting another title")
            else: # is premium member
                if len(customer.current_rentals) < 3:
                    customer.current_video_rentals = customer.current_video_rentals + "/" + video_title
                    return f"{customer.firstName} is now renting {video_title}"
                else:
                    print(f"Return one of the following titles before renting another: {customer.current_video_rentals}")
    
    def return_video(self,video_title, customer_id):
        customer_id = str(customer_id)

        if video_title in self.inventory:
            self.inventory[video_title].copies_available +=1
        #NTS: Figure out how to catch all versions of walle ( WALL-E, wall-E etc) 

            if video_title.title() in self.customers[customer_id].current_video_rentals:
                self.customers[customer_id].current_video_rentals.remove(video_title.title())
                print(self.customers[customer_id].current_video_rentals)
                return f"{video_title} was returned by {self.customers[customer_id].firstName}"
            else:
                return "Title not found in Customers current Rentals"
        else: 
            return f"{video_title} not Found in Inventory"
           # increment the invetory for the video title, remove the title from the customers rentals.
    