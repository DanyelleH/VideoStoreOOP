from classes.Inventory import Movie
from classes.Customer import Customer

class VideoStore:
    def __init__(self) -> None:
        self.customers = Customer.all_customers()
        self.Invetory = Movie.all_movies()