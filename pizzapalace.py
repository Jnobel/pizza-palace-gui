"""
Title: Pizza Palace Ordering System GUI
File: pizzapalace.py
Author: Joshua Nobel
Date: 07/10/2024
Version: 1.0

This script creates a graphical user interface (GUI) for Pizza Palace, an online pizza ordering system.
The interface includes the following screens:

1. Home Screen: Welcome message and navigation buttons to other screens.
2. Order Pizza Screen: Allows users to customize and order pizzas.
3. View Menu Screen: Displays a list of available pizzas with descriptions and prices.
4. Cart Screen: Shows the items in the user's cart with options to proceed to checkout.
5. Checkout Screen: Collects customer information and payment details.
6. Track Order Screen: Displays the order tracking status.
7. Contact Us Screen: Provides contact information and a feedback form.

"""

import tkinter as tk
from tkinter import messagebox


class PizzaPalace:
    """
    PizzaPalace class manages the entire GUI for the Pizza Palace ordering system.
    """

    def __init__(self, root):
        """
        Initializes the main application window and sets up the home screen.
        
        Parameters:
        root (tk.Tk): The main window object.
        """
        self.root = root
        self.root.title("Pizza Palace Ordering System")
        self.cart = []  # List to store cart items
        
        self.create_home_screen()

    def create_home_screen(self):
        """
        Sets up the home screen with navigation buttons to other screens.
        """
        self.clear_screen()

        # Welcome message
        tk.Label(self.root, text="Welcome to Pizza Palace!", font=("Helvetica", 16)).pack(pady=20)

        # Navigation buttons
        tk.Button(self.root, text="Order Pizza", command=self.create_order_pizza_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="View Menu", command=self.create_view_menu_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Track Order", command=self.create_track_order_screen, width=20).pack(pady=5)
        tk.Button(self.root, text="Contact Us", command=self.create_contact_us_screen, width=20).pack(pady=5)

    def create_order_pizza_screen(self):
        """
        Sets up the order pizza screen where users can customize and order pizzas.
        """
        self.clear_screen()

        # Pizza size selection
        tk.Label(self.root, text="Select Pizza Size", font=("Helvetica", 12)).pack(pady=5)
        self.size_var = tk.StringVar(value="Medium")
        sizes = [("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")]
        for text, value in sizes:
            tk.Radiobutton(self.root, text=text, variable=self.size_var, value=value).pack(anchor=tk.W)

        # Crust type selection
        tk.Label(self.root, text="Select Crust Type", font=("Helvetica", 12)).pack(pady=5)
        self.crust_var = tk.StringVar(value="Regular")
        crusts = [("Thin", "Thin"), ("Regular", "Regular"), ("Stuffed", "Stuffed")]
        for text, value in crusts:
            tk.Radiobutton(self.root, text=text, variable=self.crust_var, value=value).pack(anchor=tk.W)

        # Toppings selection
        tk.Label(self.root, text="Select Toppings", font=("Helvetica", 12)).pack(pady=5)
        self.toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Extra Cheese", "Black Olives", "Green Peppers", "Pineapple", "Spinach"]
        self.toppings_vars = []
        for topping in self.toppings:
            var = tk.BooleanVar()
            tk.Checkbutton(self.root, text=topping, variable=var).pack(anchor=tk.W)
            self.toppings_vars.append(var)

        # Quantity selection
        tk.Label(self.root, text="Select Quantity", font=("Helvetica", 12)).pack(pady=5)
        self.quantity_var = tk.IntVar(value=1)
        tk.Spinbox(self.root, from_=1, to=10, textvariable=self.quantity_var).pack()

        # Buttons to add to cart and view cart
        tk.Button(self.root, text="Add to Cart", command=self.add_to_cart).pack(pady=10)
        tk.Button(self.root, text="View Cart", command=self.create_cart_screen).pack(pady=5)
        tk.Button(self.root, text="Back to Home", command=self.create_home_screen).pack(pady=5)

    def add_to_cart(self):
        """
        Adds the selected pizza configuration to the cart and displays a confirmation message.
        """
        size = self.size_var.get()  # Get selected pizza size
        crust = self.crust_var.get()  # Get selected crust type
        toppings = [topping for topping, var in zip(self.toppings, self.toppings_vars) if var.get()]  # Get selected toppings
        quantity = self.quantity_var.get()  # Get selected quantity

        # Validate input
        if not size or not crust or quantity <= 0:
            messagebox.showwarning("Invalid Input", "Please select size, crust type, and a valid quantity.")
            return

        # Add item to cart
        item = {"size": size, "crust": crust, "toppings": toppings, "quantity": quantity}
        self.cart.append(item)
        messagebox.showinfo("Added to Cart", "Your pizza has been added to the cart.")

    def create_cart_screen(self):
        """
        Sets up the cart screen where users can review their cart items.
        """
        self.clear_screen()

        # Cart header
        tk.Label(self.root, text="Cart", font=("Helvetica", 16)).pack(pady=10)

        # Display cart items
        if not self.cart:
            tk.Label(self.root, text="Your cart is empty.").pack(pady=10)
        else:
            for index, item in enumerate(self.cart, start=1):
                text = f"Pizza {index}: Size - {item['size']}, Crust - {item['crust']}, Toppings - {', '.join(item['toppings'])}, Quantity - {item['quantity']}"
                tk.Label(self.root, text=text).pack(anchor=tk.W)

        # Buttons to proceed to checkout and go back to home
        tk.Button(self.root, text="Proceed to Checkout", command=self.create_checkout_screen).pack(pady=10)
        tk.Button(self.root, text="Back to Home", command=self.create_home_screen).pack(pady=5)

    def create_view_menu_screen(self):
        """
        Sets up the view menu screen displaying available pizzas with descriptions and prices.
        """
        self.clear_screen()

        # Menu header
        tk.Label(self.root, text="Menu", font=("Helvetica", 16)).pack(pady=10)

        # Dummy menu items
        self.menu_items = [
            {"name": "Margherita", "description": "Classic pizza with tomato sauce and mozzarella", "price": 8.99},
            {"name": "Pepperoni", "description": "Pepperoni, tomato sauce, and mozzarella", "price": 9.99},
            {"name": "BBQ Chicken", "description": "BBQ sauce, chicken, and mozzarella", "price": 10.99},
        ]

        # Display menu items
        for item in self.menu_items:
            frame = tk.Frame(self.root)
            frame.pack(pady=5, anchor=tk.W)
            tk.Label(frame, text=f"{item['name']} - ${item['price']}", font=("Helvetica", 12)).pack(side=tk.LEFT)
            tk.Button(frame, text="Add to Cart", command=lambda i=item: self.add_menu_item_to_cart(i)).pack(side=tk.RIGHT)

        # Button to go back to home
        tk.Button(self.root, text="Back to Home", command=self.create_home_screen).pack(pady=10)

    def add_menu_item_to_cart(self, item):
        """
        Adds a menu item to the cart and displays a confirmation message.
        
        Parameters:
        item (dict): The menu item to add to the cart.
        """
        self.cart.append({"size": "Medium", "crust": "Regular", "toppings": [], "quantity": 1, "name": item['name'], "price": item['price']})
        messagebox.showinfo("Added to Cart", f"{item['name']} has been added to the cart.")

    def create_track_order_screen(self):
        """
        Sets up the track order screen displaying the order tracking status.
        """
        self.clear_screen()

        # Track order header
        tk.Label(self.root, text="Track Order", font=("Helvetica", 16)).pack(pady=10)
        # Dummy tracking information
        tk.Label(self.root, text="Order #1234 - Status: Out for Delivery").pack(pady=5)

        # Button to go back to home
        tk.Button(self.root, text="Back to Home", command=self.create_home_screen).pack(pady=10)

    def create_contact_us_screen(self):
        """
        Sets up the contact us screen with contact information and a feedback form.
        """
        self.clear_screen()

        # Contact us header
        tk.Label(self.root, text="Contact Us", font=("Helvetica", 16)).pack(pady=10)

        # Contact information
        tk.Label(self.root, text="Phone: 123-456-7890").pack(pady=5)
        tk.Label(self.root, text="Email: contact@pizzapalace.com").pack(pady=5)
        tk.Label(self.root, text="Address: 123 Pizza St, Food City, FL").pack(pady=5)

        # Feedback form
        tk.Label(self.root, text="Feedback Form", font=("Helvetica", 12)).pack(pady=10)
        tk.Label(self.root, text="Name:").pack(anchor=tk.W)
        self.feedback_name_entry = tk.Entry(self.root)
        self.feedback_name_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(self.root, text="Email:").pack(anchor=tk.W)
        self.feedback_email_entry = tk.Entry(self.root)
        self.feedback_email_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(self.root, text="Message:").pack(anchor=tk.W)
        self.feedback_message_entry = tk.Text(self.root, height=5)
        self.feedback_message_entry.pack(fill=tk.X, padx=10, pady=5)

        # Button to submit feedback
        tk.Button(self.root, text="Submit", command=self.submit_feedback).pack(pady=10)
        tk.Button(self.root, text="Back to Home", command=self.create_home_screen).pack(pady=10)

    def submit_feedback(self):
        """
        Submits the feedback form and displays a confirmation message.
        """
        name = self.feedback_name_entry.get()
        email = self.feedback_email_entry.get()
        message = self.feedback_message_entry.get("1.0", tk.END).strip()

        # Validate input
        if not name or not email or not message:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields.")
            return

        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")

    def create_checkout_screen(self):
        """
        Sets up the checkout screen to collect customer information and payment details.
        """
        self.clear_screen()

        # Checkout header
        tk.Label(self.root, text="Checkout", font=("Helvetica", 16)).pack(pady=10)

        # Customer information
        tk.Label(self.root, text="Customer Information", font=("Helvetica", 12)).pack(anchor=tk.W, padx=10, pady=5)
        tk.Label(self.root, text="Name:").pack(anchor=tk.W, padx=10)
        self.checkout_name_entry = tk.Entry(self.root)
        self.checkout_name_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(self.root, text="Address:").pack(anchor=tk.W, padx=10)
        self.checkout_address_entry = tk.Entry(self.root)
        self.checkout_address_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(self.root, text="Phone:").pack(anchor=tk.W, padx=10)
        self.checkout_phone_entry = tk.Entry(self.root)
        self.checkout_phone_entry.pack(fill=tk.X, padx=10, pady=5)

        # Payment information
        tk.Label(self.root, text="Payment Information", font=("Helvetica", 12)).pack(anchor=tk.W, padx=10, pady=5)
        tk.Label(self.root, text="Credit Card Number:").pack(anchor=tk.W, padx=10)
        self.card_number_entry = tk.Entry(self.root)
        self.card_number_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(self.root, text="Expiration Date (MM/YY):").pack(anchor=tk.W, padx=10)
        self.card_expiry_entry = tk.Entry(self.root)
        self.card_expiry_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(self.root, text="CVV:").pack(anchor=tk.W, padx=10)
        self.card_cvv_entry = tk.Entry(self.root)
        self.card_cvv_entry.pack(fill=tk.X, padx=10, pady=5)

        # Button to place order
        tk.Button(self.root, text="Place Order", command=self.place_order).pack(pady=10)
        tk.Button(self.root, text="Back to Cart", command=self.create_cart_screen).pack(pady=5)

    def place_order(self):
        """
        Validates the checkout form and places the order if all fields are filled.
        """
        name = self.checkout_name_entry.get()
        address = self.checkout_address_entry.get()
        phone = self.checkout_phone_entry.get()
        card_number = self.card_number_entry.get()
        card_expiry = self.card_expiry_entry.get()
        card_cvv = self.card_cvv_entry.get()

        # Validate input
        if not name or not address or not phone or not card_number or not card_expiry or not card_cvv:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields.")
            return

        messagebox.showinfo("Order Placed", "Thank you for your order! Your pizza will be delivered soon.")
        self.cart = []  # Clear cart after placing order
        self.create_home_screen()

    def clear_screen(self):
        """
        Clears all widgets from the root window.
        """
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaPalace(root)
    root.mainloop()
