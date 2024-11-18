import csv
class Movie:
    def __init__(self,id,title,copies_available):
        self.id=id
        self.title=title.lower()
        self.copies_available = int(copies_available)

    @classmethod
    def all_movies(cls):
        inventory ={}
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/inventory.csv") as invetory_file:
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
    
    def save_to_inventory_csv(self):
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/inventory.csv", mode="w", newline='') as inventory_file:
            writer = csv.writer(inventory_file)
            writer.writerow(["id","title","copies_available"])
            for title, movie in self.inventory.items():
                writer.writerow([
                    movie.id,
                    title,
                    movie.copies_available
                ])