import csv
class Movie:
    def __init__(self,id,title,copies_available):
        self.id=id
        self.title=title
        self.copies_available = int(copies_available)

    @classmethod
    def all_movies(cls):
        invetory ={}
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/inventory.csv") as invetory_file:
            reader = csv.DictReader(invetory_file)
            for row in reader:
                movie = Movie(
                    id = row["id"],
                    title = row["title"],
                    #use integer to increment/decrement later
                    copies_available = int(row["copies_available"])
                )
                invetory[row["title"]] = movie
        return invetory