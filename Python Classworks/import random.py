class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.table_reservations = []
        self.customer_orders = []

    def add_item_to_menu(self, item):
        self.menu_items.append(item)

    def book_table(self, table_number, reservation_name):
        self.table_reservations.append((table_number, reservation_name))

    def customer_order(self, table_number, order):
        self.customer_orders.append((table_number, order))

    def print_menu(self):
        print("Menu:")
        for item in self.menu_items:
            print(item)

    def print_table_reservations(self):
        print("Table Reservations:")
        for table, name in self.table_reservations:
            print(f"Table {table}: {name}")

    def print_customer_orders(self):
        print("Customer Orders:")
        for table, order in self.customer_orders:
            print(f"Table {table} ordered: {order}")


# Create an instance of the Restaurant class
my_restaurant = Restaurant()

# Add items to the menu
my_restaurant.add_item_to_menu("Spaghetti")
my_restaurant.add_item_to_menu("Burger")
my_restaurant.add_item_to_menu("Salad")

# Make table reservations
my_restaurant.book_table(1, "John")
my_restaurant.book_table(2, "Alice")

# Take customer orders
my_restaurant.customer_order(1, "Spaghetti, Salad")
my_restaurant.customer_order(2, "Burger")

# Print the menu
my_restaurant.print_menu()

# Print table reservations
my_restaurant.print_table_reservations()

# Print customer orders
my_restaurant.print_customer_orders()