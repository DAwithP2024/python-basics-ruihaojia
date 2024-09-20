# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

# Function to display categories
def display_categories():
    print("Categories available for shopping:")
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")

# Function to display products within a category
def display_products(products_list):
    for index, product in enumerate(products_list, start=1):
        print(f"{index}. {product[0]} - ${product[1]}")

# Function to display sorted products
def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    display_products(sorted_products)
    return sorted_products

# Function to add product to cart
def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

# Function to display shopping cart
def display_cart(cart):
    if not cart:
        print("Your cart is empty.")
    else:
        print("Your shopping cart:")
        total_cost = 0
        for item in cart:
            product_name, price, quantity = item
            total_cost += price * quantity
            print(f"{product_name} - ${price} x {quantity}")
        print(f"Total cost: ${total_cost:.2f}")

# Function to generate receipt
def generate_receipt(name, email, cart, total_cost, address):
    if cart:
        print(f"\nReceipt for {name} ({email}):")
        print("Items purchased:")
        for item in cart:
            product_name, price, quantity = item
            print(f"{product_name} - ${price} x {quantity}")
        print(f"Total cost: ${total_cost:.2f}")
        print(f"Delivery address: {address}")
        print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")
    else:
        print("\nThank you for using our portal. Hope you buy something from us next time. Have a nice day.")

# Function to validate name
def validate_name(name):
    if " " in name:
        first_name, last_name = name.split()
        if first_name.isalpha() and last_name.isalpha():
            return True
    return False

# Function to validate email
def validate_email(email):
    if "@" in email:
        return True
    return False

# Main function
def main():
    # Welcome and get user's name and email
    print("Welcome to our shopping portal!")
    name = input("Please enter your name (first name and last name): ").strip()
    while not validate_name(name):
        print("Invalid name format. Please enter your full name (first name and last name) using only alphabets.")
        name = input("Please enter your name again: ").strip()

    email = input("Please enter your email address: ").strip()
    while not validate_email(email):
        print("Invalid email address format. Please enter a valid email address with '@'.")
        email = input("Please enter your email address again: ").strip()

    # Display categories for shopping
    display_categories()

    # Category selection loop
    while True:
        try:
            category_choice = int(input("Enter the number of the category you would like to explore: "))
            if category_choice < 1 or category_choice > len(products):
                raise ValueError("Invalid category number. Please enter a correct category number.")
            break
        except ValueError as e:
            print(e)
    
    selected_category = list(products.keys())[category_choice - 1]
    selected_products = products[selected_category]

    # Display products in selected category
    print(f"\nProducts available in '{selected_category}':")
    display_products(selected_products)

    cart = []

    # Shopping options loop
    while True:
        print("\nOptions:")
        print("1. Select a product to buy")
        print("2. Sort the products according to the price")
        print("3. Go back to the category selection")
        print("4. Finish shopping")

        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                # Select a product to buy
                while True:
                    try:
                        product_choice = int(input("Enter the number corresponding to the product you want to buy: "))
                        if product_choice < 1 or product_choice > len(selected_products):
                            raise ValueError("Invalid product number. Please enter a correct product number.")
                        break
                    except ValueError as e:
                        print(e)
                
                selected_product = selected_products[product_choice - 1]
                quantity = int(input(f"Enter the quantity of '{selected_product[0]}' you want to buy: "))
                add_to_cart(cart, selected_product, quantity)

            elif option == 2:
                # Sort products by price
                while True:
                    try:
                        sort_order = int(input("Sort by price: 1. Ascending 2. Descending: "))
                        if sort_order != 1 and sort_order != 2:
                            raise ValueError("Invalid sort order. Please enter 1 or 2.")
                        break
                    except ValueError as e:
                        print(e)
                
                selected_products = display_sorted_products(selected_products, sort_order)

            elif option == 3:
                # Go back to category selection
                display_categories()
                while True:
                    try:
                        category_choice = int(input("Enter the number of the category you would like to explore: "))
                        if category_choice < 1 or category_choice > len(products):
                            raise ValueError("Invalid category number. Please enter a correct category number.")
                        break
                    except ValueError as e:
                        print(e)
                
                selected_category = list(products.keys())[category_choice - 1]
                selected_products = products[selected_category]

                print(f"\nProducts available in '{selected_category}':")
                display_products(selected_products)

            elif option == 4:
                # Finish shopping
                break

            else:
                print("Invalid option. Please enter a valid option number.")
        
        except ValueError as e:
            print(e)

    # After finishing shopping
    display_cart(cart)

    if cart:
        total_cost = sum(product[1] * product[2] for product in cart)
        address = input("Please enter your delivery address: ").strip()
        generate_receipt(name, email, cart, total_cost, address)
    else:
        generate_receipt(name, email, cart, 0, "")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
