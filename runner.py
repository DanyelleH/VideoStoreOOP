from classes.Blockbuster import VideoStore
from classes.Inventory import Movie
from classes.Customer import Customer

store = VideoStore()
store.view_invetory()
# store.view_all_customers()
# store.current_rentals()
# store.new_customer("sx","jodie", "smith")
store.view_all_customers()
print(store.rent_video("WALL-E",4))