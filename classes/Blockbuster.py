from classes.Inventory import Movie
from classes.Customer import Customer
import csv

class VideoStore(Customer,Movie):
    def __init__(self) -> None:
        self.customers = Customer.all_customers() # Key: Customer id Number  value: Customer object.
        self.inventory = Movie.all_movies() # Key: Movie Title   Value: Movie object
        print("Welcome to Blockbuster! these are the menu options: ")

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

    def new_customer(self,account_type=input,first_name=input,last_name=input,current_video_rentals =""):
        account_type=input("Ener sx for Standard account, Enter px for premium account: ")
        first_name=input("Enter Customers First Name: ")
        last_name = input("Enter Customers Last Name: ")
        #Duplicate ID's wont be an issue due to customers remaining in the database, with incrementing ID's.
        #this method immediately writes the new users data to the csv file.
        id =len(self.customers) +1
        #Due to reading ssues when using class method, i decided to manually update the csv file when adding a new customer.
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/customers.csv", mode='a', newline="") as customers:
            writer = csv.writer(customers)
            writer.writerow([id,account_type,first_name,last_name,current_video_rentals])
        new_customer = Customer(id,account_type,first_name,last_name,current_video_rentals)
        #Update the list of customers in the store everytime a new user is added.
        self.customers[id] = new_customer

        print(f"New customer added: ID={id}, Name={first_name} {last_name}, Account Type={account_type}")

    def rent_video(self,video_title=input, customer_id=input):
        customer_id = input("Enter the Customers ID: ")
        if customer_id not in self.customers.keys():
            print("Invalid Customer ID Number")
            return
         
        #Formatted input so user can see the titles available to be rented
        video_title = input(f"Titles Available : {self.available_movies()}")
        if video_title not in self.available_movies():
            print(f"No copies of {video_title} available")
            return
        customer =self.customers[customer_id]
        
        current_rentals = (customer.current_video_rentals)
        if customer.account_type == "Sx":
            # handles cases where the user has no rentals in their name
            if len(current_rentals) == 1 and current_rentals[0]== "":
                print(f"{customer.firstName} is now renting {video_title}")
                customer.current_video_rentals = [video_title]
                self.inventory[video_title].copies_available -=1
            else:
                print(f"Return {customer.current_video_rentals} before renting another title")
                
        else: # is premium member
            if len(current_rentals) < 3:
                if current_rentals[0]== '':
                    customer.current_video_rentals= [video_title]
                    print(f"{customer.firstName} is now renting {video_title}, all titles currently rented are {customer.current_video_rentals}")
                    self.inventory[video_title].copies_available -=1

                else:
                    customer.current_video_rentals = customer.current_video_rentals + [video_title]
                    print(f"{customer.firstName} is now renting {video_title}, all titles currently rented are {customer.current_video_rentals}")
            else:
                print(f"Return one of the following titles before renting another: {customer.current_video_rentals}")

                '''
                Add method to update csv file with users current rentals
                '''
        self.save_to_customer_csv(customer)
        self.save_to_inventory_csv()

    def return_video(self,video_title=input, customer_id=input):
        customer_id = input("Enter Customers ID: ")
        video_title=input("What title is being returned? ")
        formatted_title = video_title.title()
        if formatted_title in self.inventory:
           # increment the invetory for the video title
            self.inventory[formatted_title].copies_available +=1
        #Note to self: Figure out how to catch all versions of walle ( WALL-E, wall-E etc) 

            if formatted_title in self.customers[customer_id].current_video_rentals:
                #remove the title from the customers rentals.
                self.customers[customer_id].current_video_rentals.remove(formatted_title)
                print(f"{formatted_title} was returned by {self.customers[customer_id].firstName} and they are still in posession of the following titles: {self.customers[customer_id].current_video_rentals}")
            else:
                print( "Title not found in Customers current Rentals")
        else: 
            print(f"{video_title} not Found in Inventory")
       

        self.save_to_customer_csv(self.customers[customer_id])
        self.save_to_inventory_csv()
    
    def available_movies(self):
        available_movies = []
        for title,movie in self.inventory.items():
            if movie.copies_available !=0:
                available_movies.append(title)
        return available_movies