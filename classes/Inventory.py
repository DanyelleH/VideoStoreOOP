import csv
class Movie:
    def __init__(self,id,title,copies_available):
        self.id=id
        self.title=title
        self.copies_available = copies_available

    @classmethod
    def all_movies(cls):
        invetory =[]
        with open("/Users/danyelleridley/GolfPlatoonImmersive/Module_1_Fundamentals/assessment-2/data/inventory.csv") as invetory_file:
            reader = csv.DictReader(invetory_file)
            for row in reader:
                invetory.append(Movie(**row))
        return invetory