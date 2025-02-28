Video Inventory Manager.  <br>Object Oriented Programming + CSV Reading




#### customer.csv
- id
- account_type 
- first_name 
- last_name 
- current_video_rentals (list of titles separated by '/')

#### inventory.csv
- id 
- title 
- copies_available 

### Data Management
Your Video Inventory Management application manages the following data:

- Manage customer information:
  - customer id
  - customer account type (sx/px)
    - "sx" = standard account: max 1 rental out at a time
    - "px" = premium account: max 3 rentals out at a time 
  - customer first name
  - customer last name 
  - current list of video rentals (*by title*)
- Manage the store's video inventory:
  - video id
  - video title
  - number of copies currently available in-store
  
### Application Features
The application allows: 
1. Viewing the current video inventory for the store
    - show `title` and `copies_available` for each video in the inventory
2. Viewing all customers
    - show `customer_id` and `name` for each customer in the store
3. Viewing a customer's current rented videos
    - take in a `customer_id` from the user and show current rented videos for that customer
    - each title should be listed separately (i.e. not displayed as one string with slashes straight from the CSV file)
4. Adding a new customer
    - a newly created customer should not have any rentals 
    - can you prevent duplicate ids from existing?
5. Renting a video out to a customer
    - video *by `title`*
    - customer *by `id`*
    - **IMPORTANT:** Customers should be limited based on their account type. Your application should enforce these limitations when attempting to rent a video!
6. Returning a video from a customer
    - video *by `title`*
    - customer *by `id`*
7. Exiting the application

# User Menu
```
== Welcome to Code Platoon Video! ==
1. View store video inventory
2. View store customers
3. View customer rented videos
4. Add new customer
5. Rent video
6. Return video
7. Exit
```
