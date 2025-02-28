import csv
import os
base_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
inventory_path= os.path.join(base_dir, "MoviesDatabase/data/inventory.csv")
class Movie:
    def __init__(self,id,title,copies_available):
        self.id=id
        self.title=title.lower()
        self.copies_available = int(copies_available)

    @classmethod
    def all_movies(cls):
        inventory ={}
        with open(inventory_path) as invetory_file:
            reader = csv.DictReader(invetory_file)
            for row in reader:
                movie = Movie(
                    id = row["id"],
                    title = row["title"],
                    #use integer to increment/decrement later
                    copies_available = int(row["copies_available"])
                )
                inventory[row["title"]] = movie
        return inventory
    