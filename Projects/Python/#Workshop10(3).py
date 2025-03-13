class Restaurant:
    def __init__(self):
        self.menu_items = []
        self.book_table = []
        self.customer_orders = []
       
    def add_item_to_menu(self, foodName):
        self.menu_items.append(foodName)

    def book_table(self, table_number, customerName):
        self.table_reservations.append((table_number, customerName))

    def customer_order(self, customerName, customer_order):
        self.customer_orders.append((customerName, customer_order))
     
    def print_menu(self):
        print("Menu: ")
        for item in self.menu_items:
            print(item)

    def print_table_reservations(self):
        print("Table Reservations: ")
        for table in self.booked_tables:
            print(f"Table {table} is booked.")

    def print_customer_orders(self):
        print("Customer Orders:")
        for table, order in self.customer_orders:
            print(f"Table {table} ordered: {order}")

restaurant = Restaurant()

#Add items to menu
restaurant.add_item_to_menu("Spaghetti Bolognese")
restaurant.add_item_to_menu("Vegan Burger")
restaurant.add_item_to_menu("Caesar Salad")

#Make table reservations
restaurant.book_table(1, "Chantal")
restaurant.book_table(2, "Munira")

#Customer's orders
restaurant.customer_order(1, "Curry Chicken, Naan Bread")
restaurant.customer_order(2, "Shrimp ALfredo Pasta")

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()