import csv

class Customer:
    def __init__(self,id,account_type,first_name,last_name,current_video_rentals):
        self.id = id
        self.account_type = account_type
        self.firstName = first_name
        self.lastName = last_name
        self.current_video_rentals = current_video_rentals
    
    @classmethod
    def all_customers(cls):
        customers =[]
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/customers.csv") as customer_file:
            reader = csv.DictReader(customer_file)
            for row in reader:
                customers.append(Customer(**row))
        return customers