import csv
import os
base_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
customer_path= os.path.join(base_dir, "data/customers.csv")

class Customer:
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals):
        self.id = str(id)
        self.account_type = account_type.lower()
        self.firstName = first_name.title()
        self.lastName = last_name.title()
        #added split method to prevent having to worry about "/" in folowing functions
        self.current_video_rentals = current_video_rentals
    
    @classmethod
    def all_customers(cls):
        customers = {} #Key: customer_id, Value = Dictionary of customers info
        with open(customer_path) as customer_file:
            reader = csv.DictReader(customer_file)
            for row in reader:
                '''
                each row is a customer. Create a dictionary to allow us to easily access
                customers information.
                -   Due to persistent errors with creating new customers, each attibute
                    is assigned manually instead of args/kwargs.
                '''
                customer = Customer(
                    id= str(row["id"]),
                    account_type=row["account_type"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    current_video_rentals=row["current_video_rentals"]
                )
                customers[customer.id] = customer
        return customers