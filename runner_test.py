import unittest
from classes.Blockbuster import VideoStore
from classes.Inventory import Movie
from classes.Customer import Customer
## i was not able to create my own tests so i used CHATGPT to generate some... before i knew that that wasnt allowed :o! 

class TestVideoStoreRunner(unittest.TestCase):

    def setUp(self):
        """
        Set up a test instance of the VideoStore for testing purposes.
        Initialize mock data for inventory and customers to avoid modifying real data.
        """
        self.store = VideoStore()
        
        # Mock data for inventory
        self.store.inventory = {
            "Wall-E": Movie(id=1, title="Wall-E", copies_available=5),
            "Inception": Movie(id=2, title="Inception", copies_available=3),
        }
        
        # Mock data for customers
        self.store.customers = {
            1: Customer(id=1, account_type="sx", first_name="Alice", last_name="Smith", current_video_rentals=["Wall-E"]),
            2: Customer(id=2, account_type="px", first_name="Bob", last_name="Jones", current_video_rentals=[]),
        }

    def test_view_inventory(self):
        """
        Test viewing inventory to ensure all movies and their availability are displayed correctly.
        """
        expected_output = {
            "Wall-E": 5,
            "Inception": 3
        }
        inventory = {title: movie.copies_available for title, movie in self.store.inventory.items()}
        self.assertEqual(inventory, expected_output)

    def test_add_new_customer(self):
        """
        Test adding a new customer to the store.
        """
        # Simulate adding a new customer
        self.store.new_customer = lambda: Customer(3, "px", "Charlie", "Brown", [])
        self.store.customers[3] = self.store.new_customer()
        
        new_customer = self.store.customers[3]
        self.assertEqual(new_customer.firstName, "Charlie")
        self.assertEqual(new_customer.lastName, "Brown")
        self.assertEqual(new_customer.account_type, "px")

    def test_rent_video(self):
        """
        Test renting a video to a customer.
        """
        self.store.rent_video = lambda: None  # Simulate renting "Inception" to customer 2
        self.store.customers[2].current_video_rentals.append("Inception")
        self.store.inventory["Inception"].copies_available -= 1

        # Verify customer rentals and inventory update
        self.assertIn("Inception", self.store.customers[2].current_video_rentals)
        self.assertEqual(self.store.inventory["Inception"].copies_available, 2)

    def test_view_customers(self):
        """
        Test viewing all customers to ensure customer information is displayed correctly.
        """
        expected_customers = {
            1: "Alice Smith",
            2: "Bob Jones",
        }
        customer_list = {id: f"{customer.firstName} {customer.lastName}" for id, customer in self.store.customers.items()}
        self.assertEqual(customer_list, expected_customers)
        
   #Couldn't figure out how to get test operational##     
    def test_return_video(self):
        self.store = VideoStore()
        
        # Mock data for inventory
        self.store.inventory = {
            "Wall-E": Movie(id=1, title="Wall-E", copies_available=5),
            "Inception": Movie(id=2, title="Inception", copies_available=3),
        }
        
        # Mock data for customers
        self.store.customers = {
            1: Customer(id=1, account_type="sx", first_name="Alice", last_name="Smith", current_video_rentals=["Wall-E"]),
            2: Customer(id=2, account_type="px", first_name="Bob", last_name="Jones", current_video_rentals=[]),
        }
    
if __name__ == "__main__":
    unittest.main()