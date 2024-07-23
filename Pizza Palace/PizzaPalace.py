"""
Title: Pizza Palace Ordering System GUI
File: PizzaPalace.py
Author: Joshua Nobel
Date: 07/22/2024
Version: 1.0

This script creates a graphical user interface (GUI) for Pizza Palace, an online pizza ordering system.
The interface includes the following screens:

1. Home Screen: Welcome message and navigation buttons to other screens.
2. Order Pizza Screen: Allows users to customize and order pizzas.
3. View Menu Screen: Displays a list of available pizzas with descriptions and prices.
4. View Beverages Screen: Displays a list of available beverages with descriptions and prices.
4. Cart Screen: Shows the items in the user's cart with options to proceed to checkout.
5. Checkout Screen: Collects customer information and payment details.
6. Track Order Screen: Displays the order tracking status.
7. Contact Us Screen: Provides contact information and a feedback form.
8. Login screen: Sign in or register for account and order history.
"""


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

class PizzaPalace:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Palace Ordering System")
        self.root.geometry("1000x1200")
        self.root.configure(bg="#FFE461")
        self.cart = []
        self.users = {}
        self.current_user = None
        self.load_users()
        self.load_images()
        self.create_home_screen()

    def load_images(self):
        try:
            self.logo_image = Image.open("logo.JPG")
            self.logo_photo = ImageTk.PhotoImage(self.logo_image)

            self.toppings_images = {
                "Bacon": ImageTk.PhotoImage(Image.open("bacon.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Black Olives": ImageTk.PhotoImage(Image.open("black olives.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Extra Cheese": ImageTk.PhotoImage(Image.open("extra cheese.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Green Peppers": ImageTk.PhotoImage(Image.open("green peppers.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Mushrooms": ImageTk.PhotoImage(Image.open("mushrooms.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Onions": ImageTk.PhotoImage(Image.open("onions.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Pepperoni": ImageTk.PhotoImage(Image.open("pepperoni.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Pineapple": ImageTk.PhotoImage(Image.open("pineapple.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Ham": ImageTk.PhotoImage(Image.open("ham.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Sausage": ImageTk.PhotoImage(Image.open("sausage.png").resize((50, 50), Image.Resampling.LANCZOS)),
                "Spinach": ImageTk.PhotoImage(Image.open("spinach.png").resize((50, 50), Image.Resampling.LANCZOS))
            }

            self.menu_images = {
                "BBQ Chicken": ImageTk.PhotoImage(Image.open("BBQChicken.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Charcoal": ImageTk.PhotoImage(Image.open("Charcoal.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Cheesey": ImageTk.PhotoImage(Image.open("Cheesey.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Flaming Pork": ImageTk.PhotoImage(Image.open("Flaming Pork.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Hawaiian": ImageTk.PhotoImage(Image.open("Hawaiian.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Margherita": ImageTk.PhotoImage(Image.open("MargheritaPizza.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Meat Lovers": ImageTk.PhotoImage(Image.open("MeatLovers.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Pepperoni": ImageTk.PhotoImage(Image.open("PepperoniPizza.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Seafood": ImageTk.PhotoImage(Image.open("Seafood.png").resize((100, 100), Image.Resampling.LANCZOS)),
                "Supreme": ImageTk.PhotoImage(Image.open("Supreme.png").resize((100, 100), Image.Resampling.LANCZOS))
            }

            self.beverage_images = {
                "Coke": ImageTk.PhotoImage(Image.open("coke.png").resize((200, 100), Image.Resampling.LANCZOS)),
                "Jarritos": ImageTk.PhotoImage(Image.open("jarritos.png").resize((200, 100), Image.Resampling.LANCZOS))
            }

            self.map_image = ImageTk.PhotoImage(Image.open("map.PNG").resize((800, 400), Image.Resampling.LANCZOS))
            print("Images loaded successfully")

        except Exception as e:
            print(f"Error loading images: {e}")

    def load_users(self):
        try:
            with open("users.json", "r") as f:
                self.users = json.load(f)
        except FileNotFoundError:
            self.users = {}

    def save_users(self):
        with open("users.json", "w") as f:
            json.dump(self.users, f)

    def create_home_screen(self):
        self.clear_screen()

        tk.Label(self.root, image=self.logo_photo, bg="#FFE461").pack(pady=10)
        tk.Label(self.root, text="Welcome to Pizza Palace!", font=("Cooper Black", 36), bg="#FFE461").pack(pady=20)

        button_frame = tk.Frame(self.root, bg="#FFE461")
        button_frame.pack(pady=10)

        buttons = [
            ("Menu", self.create_order_pizza_screen),
            ("Specialty Menu", self.create_view_menu_screen),
            ("Beverages", self.create_order_beverage_screen),
            ("Track Order", self.create_track_order_screen),
            ("Contact Us", self.create_contact_us_screen),
            ("Login", self.create_login_screen),
            ("Order History", self.create_order_history_screen)
        ]

        for i, (text, command) in enumerate(buttons):
            row = i // 3
            col = i % 3
            tk.Button(button_frame, text=text, command=command, width=20).grid(row=row, column=col, padx=5, pady=5)

    def create_order_pizza_screen(self):
        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Select Pizza Size", font=("Cooper Black", 12), bg="#FFE461").pack(pady=5)
        self.size_var = tk.StringVar(value="Medium")
        sizes = [("Small", "Small"), ("Medium", "Medium"), ("Large", "Large")]
        for text, value in sizes:
            tk.Radiobutton(frame, text=text, variable=self.size_var, value=value, bg="#FFE461").pack(anchor=tk.W)

        tk.Label(frame, text="Select Crust Type", font=("Cooper Black", 12), bg="#FFE461").pack(pady=5)
        self.crust_var = tk.StringVar(value="Regular")
        crusts = [("Thin", "Thin"), ("Regular", "Regular"), ("Stuffed", "Stuffed +$2")]
        for text, value in crusts:
            tk.Radiobutton(frame, text=text, variable=self.crust_var, value=value, bg="#FFE461").pack(anchor=tk.W)

        tk.Label(frame, text="Select Toppings", font=("Cooper Black", 12), bg="#FFE461").pack(pady=5)
        self.toppings = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Bacon", "Extra Cheese", "Black Olives", "Green Peppers", "Pineapple", "Spinach", "Ham"]
        self.toppings_vars = []
        for topping in self.toppings:
            var = tk.BooleanVar()
            topping_frame = tk.Frame(frame, bg="#FFE461")
            topping_frame.pack(anchor=tk.W)
            tk.Checkbutton(topping_frame, text=topping, variable=var, bg="#FFE461").pack(side=tk.LEFT)
            tk.Label(topping_frame, image=self.toppings_images.get(topping), bg="#FFE461").pack(side=tk.RIGHT)
            self.toppings_vars.append(var)

        tk.Label(frame, text="Select Quantity", font=("Cooper Black", 12), bg="#FFE461").pack(pady=5)
        self.quantity_var = tk.IntVar(value=1)
        tk.Spinbox(frame, from_=1, to=10, textvariable=self.quantity_var).pack()

        tk.Button(frame, text="Add to Cart", command=self.add_pizza_to_cart).pack(pady=10)
        tk.Button(frame, text="View Cart", command=self.create_cart_screen).pack(pady=5)
        tk.Button(frame, text="Back to Home", command=self.create_home_screen).pack(pady=5)

    def add_pizza_to_cart(self):
        size = self.size_var.get()
        crust = self.crust_var.get().replace(" +$2", "")
        toppings = [topping for topping, var in zip(self.toppings, self.toppings_vars) if var.get()]
        quantity = self.quantity_var.get()

        if not size or not crust or quantity <= 0:
            messagebox.showwarning("Invalid Input", "Please select size, crust type, and a valid quantity.")
            return

        base_price = {"Small": 10.99, "Medium": 12.99, "Large": 14.99}
        crust_price = 2.0 if crust == "Stuffed" else 0.0
        price = base_price[size] + crust_price + 1.5 * len(toppings)

        item = {"type": "pizza", "size": size, "crust": crust, "toppings": toppings, "quantity": quantity, "price": price}
        self.cart.append(item)
        messagebox.showinfo("Added to Cart", "Your pizza has been added to the cart.")

    def create_order_beverage_screen(self):
        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Select Beverage", font=("Cooper Black", 12), bg="#FFE461").pack(pady=5)

        tk.Label(frame, image=self.beverage_images["Coke"], bg="#FFE461").pack()
        self.beverage_var = tk.StringVar(value="None")
        coke_flavors = ["None", "Diet Coke", "Coca-cola", "Dr. Pepper", "Sunkist", "Squirt", "Sprite"]
        for flavor in coke_flavors:
            tk.Radiobutton(frame, text=flavor, variable=self.beverage_var, value=flavor, bg="#FFE461").pack(anchor=tk.W)

        tk.Label(frame, image=self.beverage_images["Jarritos"], bg="#FFE461").pack()
        jarritos_flavors = ["None", "Tamarind", "Strawberry", "Mandarin", "Grapefruit", "Fruit Punch"]
        for flavor in jarritos_flavors:
            tk.Radiobutton(frame, text=flavor, variable=self.beverage_var, value=flavor, bg="#FFE461").pack(anchor=tk.W)

        tk.Label(frame, text="Beverage Quantity", font=("Cooper Black", 12), bg="#FFE461").pack(pady=5)
        self.beverage_quantity_var = tk.IntVar(value=1)
        tk.Spinbox(frame, from_=1, to=10, textvariable=self.beverage_quantity_var).pack()

        tk.Button(frame, text="Add to Cart", command=self.add_beverage_to_cart).pack(pady=10)
        tk.Button(frame, text="View Cart", command=self.create_cart_screen).pack(pady=5)
        tk.Button(frame, text="Back to Home", command=self.create_home_screen).pack(pady=5)

    def add_beverage_to_cart(self):
        beverage = self.beverage_var.get()
        beverage_quantity = self.beverage_quantity_var.get()

        if beverage == "None" or beverage_quantity <= 0:
            messagebox.showwarning("Invalid Input", "Please select a beverage and a valid quantity.")
            return

        beverage_price = 1.75 if beverage in ["Tamarind", "Strawberry", "Mandarin", "Grapefruit", "Fruit Punch"] else 1.0
        price = beverage_price * beverage_quantity

        item = {"type": "beverage", "beverage": beverage, "beverage_quantity": beverage_quantity, "price": price}
        self.cart.append(item)
        messagebox.showinfo("Added to Cart", "Your beverage has been added to the cart.")

    def create_cart_screen(self):
        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Cart", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        if not self.cart:
            tk.Label(frame, text="Your cart is empty.", bg="#FFE461").pack(pady=10)
        else:
            self.cart_frames = []
            for index, item in enumerate(self.cart):
                item_frame = tk.Frame(frame, bg="#FFE461")
                item_frame.pack(fill=tk.X, pady=5)
                self.cart_frames.append(item_frame)

                if item['type'] == 'pizza':
                    item_text = f"Pizza {index + 1}: Size - {item['size']}, Crust - {item['crust']}, Toppings - {', '.join(item['toppings'])}, Quantity - {item['quantity']}, Price - ${item['price'] * item['quantity']:.2f}"
                else:
                    item_text = f"Beverage {index + 1}: {item['beverage']} x {item['beverage_quantity']}, Price - ${item['price']:.2f}"
                tk.Label(item_frame, text=item_text, bg="#FFE461").pack(side=tk.LEFT)

                tk.Button(item_frame, text="Edit", command=lambda i=index: self.edit_cart_item(i)).pack(side=tk.LEFT, padx=5)
                tk.Button(item_frame, text="Remove", command=lambda i=index: self.remove_cart_item(i)).pack(side=tk.LEFT, padx=5)

            self.update_cart_total()

        tk.Button(frame, text="Proceed to Checkout", command=self.create_checkout_screen).pack(pady=10)
        tk.Button(frame, text="Back to Home", command=self.create_home_screen).pack(pady=5)

    def edit_cart_item(self, index):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Item")

        if self.cart[index]['type'] == 'pizza':
            tk.Label(edit_window, text="Quantity:").pack(pady=5)
            quantity_var = tk.IntVar(value=self.cart[index]['quantity'])
            tk.Spinbox(edit_window, from_=1, to=10, textvariable=quantity_var).pack(pady=5)
            tk.Button(edit_window, text="Update", command=lambda: self.update_cart_item(index, quantity_var.get(), edit_window)).pack(pady=10)
        else:
            tk.Label(edit_window, text="Beverage Quantity:").pack(pady=5)
            beverage_quantity_var = tk.IntVar(value=self.cart[index]['beverage_quantity'])
            tk.Spinbox(edit_window, from_=1, to=10, textvariable=beverage_quantity_var).pack(pady=5)
            tk.Button(edit_window, text="Update", command=lambda: self.update_cart_item(index, beverage_quantity_var.get(), edit_window)).pack(pady=10)

    def update_cart_item(self, index, new_quantity, window):
        if self.cart[index]['type'] == 'pizza':
            self.cart[index]['quantity'] = new_quantity
        else:
            self.cart[index]['beverage_quantity'] = new_quantity
            beverage_price = 1.75 if self.cart[index]['beverage'] in ["Tamarind", "Strawberry", "Mandarin", "Grapefruit", "Fruit Punch"] else 1.0
            self.cart[index]['price'] = beverage_price * new_quantity
        window.destroy()
        self.create_cart_screen()

    def remove_cart_item(self, index):
        del self.cart[index]
        self.create_cart_screen()

    def update_cart_total(self):
        subtotal = sum(item['price'] * (item['quantity'] if item['type'] == 'pizza' else 1) for item in self.cart)
        tax = subtotal * 0.07
        total = subtotal + tax

        frame = tk.Frame(self.root, bg="#FFE461")
        frame.pack(fill=tk.X, pady=5)
        self.cart_frames.append(frame)

        tk.Label(frame, text=f"Subtotal: ${subtotal:.2f}", bg="#FFE461").pack(anchor=tk.E)
        tk.Label(frame, text=f"Tax: ${tax:.2f}", bg="#FFE461").pack(anchor=tk.E)
        tk.Label(frame, text=f"Total: ${total:.2f}", bg="#FFE461").pack(anchor=tk.E)

    def create_view_menu_screen(self):
        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Menu", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        self.menu_items = [
            {"name": "BBQ Chicken", "description": "BBQ sauce, chicken, and mozzarella", "price": 16.99, "image": "BBQ Chicken"},
            {"name": "Charcoal", "description": "Charcoal crust, smoky flavor", "price": 27.99, "image": "Charcoal"},
            {"name": "Cheesey", "description": "Extra cheese and mozzarella", "price": 14.99, "image": "Cheesey"},
            {"name": "Flaming Pork", "description": "Spicy pork and hot sauce", "price": 17.99, "image": "Flaming Pork"},
            {"name": "Hawaiian", "description": "Ham, pineapple, and mozzarella", "price": 15.99, "image": "Hawaiian"},
            {"name": "Margherita", "description": "Classic pizza with tomato sauce and mozzarella", "price": 15.99, "image": "Margherita"},
            {"name": "Meat Lovers", "description": "Pepperoni, sausage, bacon, and ham", "price": 16.99, "image": "Meat Lovers"},
            {"name": "Pepperoni", "description": "Pepperoni, tomato sauce, and mozzarella", "price": 15.99, "image": "Pepperoni"},
            {"name": "Seafood", "description": "Shrimp, calamari, and mozzarella", "price": 19.99, "image": "Seafood"},
            {"name": "Supreme", "description": "Pepperoni, sausage, green peppers, onions, and mushrooms", "price": 17.99, "image": "Supreme"}
        ]

        self.size_prices = {
            "Small": -4.0,
            "Medium": -2.0,
            "Large": 0.0
        }
        
        self.crust_prices = {
            "Thin": 0.0,
            "Regular": 0.0,
            "Stuffed": 2.0
        }

        self.size_vars = {}
        self.crust_vars = {}
        self.price_labels = {}

        for item in self.menu_items:
            item_frame = tk.Frame(frame, padx=150, pady=5, bg="#FFE461", highlightbackground="red", highlightthickness=2)
            item_frame.pack(fill=tk.X, pady=5)
            item_frame.configure(height=200)
            size_var = tk.StringVar(value="Large")
            self.size_vars[item["name"]] = size_var
            crust_var = tk.StringVar(value="Regular")
            self.crust_vars[item["name"]] = crust_var

            try:
                img = self.menu_images[item["image"]]
                img_label = tk.Label(item_frame, image=img, bg="#FFE461")
                img_label.image = img  # Keep a reference to avoid garbage collection
                img_label.pack(side=tk.LEFT, padx=10)
            except KeyError:
                print(f"Image for {item['name']} not found")

            text_frame = tk.Frame(item_frame, bg="#FFE461")
            text_frame.pack(side=tk.LEFT, fill=tk.X)

            tk.Label(text_frame, text=f"{item['name']}", font=("Cooper Black", 12), bg="#FFE461").pack(anchor=tk.W)
            tk.Label(text_frame, text=item["description"], bg="#FFE461", wraplength=300, justify=tk.LEFT).pack(anchor=tk.W)
            
            size_frame = tk.Frame(text_frame, bg="#FFE461")
            size_frame.pack(fill=tk.X)
            for size in self.size_prices:
                tk.Radiobutton(size_frame, text=size, variable=size_var, value=size, command=lambda i=item, sv=size_var, cv=crust_var: self.update_price(i, sv, cv), bg="#FFE461").pack(side=tk.LEFT)

            crust_frame = tk.Frame(text_frame, bg="#FFE461")
            crust_frame.pack(fill=tk.X)
            for crust in self.crust_prices:
                tk.Radiobutton(crust_frame, text=crust, variable=crust_var, value=crust, command=lambda i=item, sv=size_var, cv=crust_var: self.update_price(i, sv, cv), bg="#FFE461").pack(side=tk.LEFT)

            price_label = tk.Label(text_frame, text=f"${item['price']:.2f}", font=("Cooper Black", 12), bg="#FFE461")
            price_label.pack(anchor=tk.E)
            self.price_labels[item["name"]] = price_label

            tk.Button(text_frame, text="Add to Cart", command=lambda i=item: self.add_menu_item_to_cart(i)).pack(anchor=tk.E)

        tk.Button(frame, text="View Cart", command=self.create_cart_screen).pack(pady=10)
        tk.Button(frame, text="Back to Home", command=self.create_home_screen).pack(pady=10)

    def update_price(self, item, size_var, crust_var):
        base_price = item['price']
        size = size_var.get()
        crust = crust_var.get()
        new_price = base_price + self.size_prices[size] + self.crust_prices[crust]
        self.price_labels[item["name"]].config(text=f"${new_price:.2f}")

    def add_menu_item_to_cart(self, item):
        size = self.size_vars[item["name"]].get()
        crust = self.crust_vars[item["name"]].get()
        base_price = item['price']
        price = base_price + self.size_prices[size] + self.crust_prices[crust]
        self.cart.append({"type": "pizza", "size": size, "crust": crust, "toppings": [], "quantity": 1, "name": item['name'], "price": price})
        messagebox.showinfo("Added to Cart", f"{item['name']} has been added to the cart.")

    def create_track_order_screen(self):
        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Track Order", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        tk.Label(frame, text="Order #1234 - Status: Out for Delivery", bg="#FFE461").pack(pady=5)

        self.tracking_canvas = tk.Canvas(frame, width=800, height=400)
        self.tracking_canvas.pack()
        self.tracking_canvas.create_image(0, 0, anchor=tk.NW, image=self.map_image)

        self.tracking_canvas.create_oval(340, 190, 360, 210, fill="red")  # Order location
        self.tracking_canvas.create_oval(40, 40, 60, 60, fill="green")   # Starting point
        self.tracking_canvas.create_line(50, 50, 350, 200, fill="blue", dash=(4, 2))

        self.remaining_time_label = tk.Label(frame, text="Time Remaining: 10 min", font=("Cooper Black", 12), bg="#FFE461")
        self.remaining_time_label.pack(pady=10)
        self.update_timer(600)

        tk.Button(frame, text="Message", command=self.send_message).pack(side=tk.LEFT, padx=10)
        tk.Button(frame, text="Change Address", command=self.change_address).pack(side=tk.RIGHT, padx=10)

        tk.Button(frame, text="Back to Home", command=self.create_home_screen).pack(pady=10)

    def update_timer(self, remaining_time):
        if remaining_time > 0:
            mins, secs = divmod(remaining_time, 60)
            time_format = f"Time Remaining: {mins} min {secs} sec"
            self.remaining_time_label.config(text=time_format)
            self.root.after(1000, self.update_timer, remaining_time - 1)
        else:
            self.remaining_time_label.config(text="Order Delivered!")

    def send_message(self):
        message_window = tk.Toplevel(self.root)
        message_window.title("Send Message")

        tk.Label(message_window, text="Type your message:").pack(pady=5)
        message_text = tk.Text(message_window, width=40, height=10)
        message_text.pack(pady=5)

        tk.Button(message_window, text="Send", command=lambda: self.submit_message(message_text.get("1.0", tk.END), message_window)).pack(pady=10)

    def submit_message(self, message, window):
        if message.strip():
            messagebox.showinfo("Message Sent", "Your message has been sent to the delivery driver.")
            window.destroy()
        else:
            messagebox.showwarning("Empty Message", "Please type a message before sending.")

    def change_address(self):
        change_address_window = tk.Toplevel(self.root)
        change_address_window.title("Change Address")

        tk.Label(change_address_window, text="New Address:").pack(pady=5)
        new_address_entry = tk.Entry(change_address_window, width=50)
        new_address_entry.pack(pady=5)
        tk.Button(change_address_window, text="Submit", command=lambda: self.submit_new_address(new_address_entry.get(), change_address_window)).pack(pady=10)

    def submit_new_address(self, new_address, window):
        if new_address:
            messagebox.showinfo("Address Updated", f"Your address has been updated to: {new_address}")
            window.destroy()
        else:
            messagebox.showwarning("Invalid Address", "Please enter a valid address.")


    def create_contact_us_screen(self):
        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Contact Us", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        tk.Label(frame, text="Phone: 812-555-1234", bg="#FFE461").pack(pady=5)
        tk.Label(frame, text="Email: contact@pizzapalace.com", bg="#FFE461").pack(pady=5)
        tk.Label(frame, text="Address: 123 Pizza St, Pizza City, IN", bg="#FFE461").pack(pady=5)

        tk.Label(frame, text="Feedback Form", font=("Cooper Black", 12), bg="#FFE461").pack(pady=10)
        tk.Label(frame, text="Name:", bg="#FFE461").pack(anchor=tk.W)
        self.feedback_name_entry = tk.Entry(frame)
        self.feedback_name_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="Email:", bg="#FFE461").pack(anchor=tk.W)
        self.feedback_email_entry = tk.Entry(frame)
        self.feedback_email_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="Message:", bg="#FFE461").pack(anchor=tk.W)
        self.feedback_message_entry = tk.Text(frame, height=5)
        self.feedback_message_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Button(frame, text="Submit", command=self.submit_feedback).pack(pady=10)
        tk.Button(frame, text="Back to Home", command=self.create_home_screen).pack(pady=10)

    def submit_feedback(self):
        name = self.feedback_name_entry.get()
        email = self.feedback_email_entry.get()
        message = self.feedback_message_entry.get("1.0", tk.END).strip()

        if not name or not email or not message:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields.")
            return

        messagebox.showinfo("Feedback Submitted", "Thank you for your feedback!")

    def create_checkout_screen(self):
        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Checkout", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        tk.Label(frame, text="Customer Information", font=("Cooper Black", 12), bg="#FFE461").pack(anchor=tk.W, padx=10, pady=5)
        tk.Label(frame, text="Name:", bg="#FFE461").pack(anchor=tk.W, padx=10)
        self.checkout_name_entry = tk.Entry(frame)
        self.checkout_name_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="Address:", bg="#FFE461").pack(anchor=tk.W, padx=10)
        self.checkout_address_entry = tk.Entry(frame)
        self.checkout_address_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="Phone:", bg="#FFE461").pack(anchor=tk.W, padx=10)
        self.checkout_phone_entry = tk.Entry(frame)
        self.checkout_phone_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="Payment Information", font=("Cooper Black", 12), bg="#FFE461").pack(anchor=tk.W, padx=10, pady=5)
        tk.Label(frame, text="Credit Card Number:", bg="#FFE461").pack(anchor=tk.W, padx=10)
        self.card_number_entry = tk.Entry(frame)
        self.card_number_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="Expiration Date (MM/YY):", bg="#FFE461").pack(anchor=tk.W, padx=10)
        self.card_expiry_entry = tk.Entry(frame)
        self.card_expiry_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(frame, text="CVV:", bg="#FFE461").pack(anchor=tk.W, padx=10)
        self.card_cvv_entry = tk.Entry(frame)
        self.card_cvv_entry.pack(fill=tk.X, padx=10, pady=5)

        tk.Button(frame, text="Place Order", command=self.place_order).pack(pady=10)
        tk.Button(frame, text="Back to Cart", command=self.create_cart_screen).pack(pady=5)

    def place_order(self):
        name = self.checkout_name_entry.get()
        address = self.checkout_address_entry.get()
        phone = self.checkout_phone_entry.get()
        card_number = self.card_number_entry.get()
        card_expiry = self.card_expiry_entry.get()
        card_cvv = self.card_cvv_entry.get()

        if not name or not address or not phone or not card_number or not card_expiry or not card_cvv:
            messagebox.showwarning("Incomplete Form", "Please fill out all fields.")
            return

        if self.current_user:
            if 'order_history' not in self.users[self.current_user]:
                self.users[self.current_user]['order_history'] = []
            self.users[self.current_user]['order_history'].append(self.cart.copy())
            self.save_users()

        messagebox.showinfo("Order Placed", "Thank you for your order! Your pizza will be delivered soon.")
        self.cart = []
        self.create_home_screen()


    def create_login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Login", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        tk.Label(self.root, text="Username:", bg="#FFE461").pack(pady=5)
        self.login_username_entry = tk.Entry(self.root)
        self.login_username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#FFE461").pack(pady=5)
        self.login_password_entry = tk.Entry(self.root, show="*")
        self.login_password_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)
        tk.Button(self.root, text="Register", command=self.create_register_screen).pack(pady=5)
        tk.Button(self.root, text="Back to Home", command=self.create_home_screen).pack(pady=5)

    def login(self):
        username = self.login_username_entry.get()
        password = self.login_password_entry.get()

        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            messagebox.showinfo("Login Successful", f"Welcome, {username}!")
            self.create_home_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def create_register_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Register", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        tk.Label(self.root, text="Username:", bg="#FFE461").pack(pady=5)
        self.register_username_entry = tk.Entry(self.root)
        self.register_username_entry.pack(pady=5)

        tk.Label(self.root, text="Password:", bg="#FFE461").pack(pady=5)
        self.register_password_entry = tk.Entry(self.root, show="*")
        self.register_password_entry.pack(pady=5)

        tk.Button(self.root, text="Register", command=self.register).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.create_login_screen).pack(pady=5)

    def register(self):
        username = self.register_username_entry.get()
        password = self.register_password_entry.get()

        if username in self.users:
            messagebox.showerror("Registration Failed", "Username already exists.")
        else:
            self.users[username] = {"password": password, "order_history": []}
            self.save_users()
            messagebox.showinfo("Registration Successful", "You can now log in.")
            self.create_login_screen()

    def create_order_history_screen(self):
        if not self.current_user:
            messagebox.showwarning("Login Required", "Please log in to view your order history.")
            self.create_login_screen()
            return

        self.clear_screen()
        canvas, frame = self.create_scrollable_canvas()

        tk.Label(frame, text="Order History", font=("Cooper Black", 16), bg="#FFE461").pack(pady=10)

        if "order_history" not in self.users[self.current_user] or not self.users[self.current_user]["order_history"]:
            tk.Label(frame, text="You have no order history.", bg="#FFE461").pack(pady=10)
        else:
            for order_index, order in enumerate(self.users[self.current_user]["order_history"]):
                order_frame = tk.Frame(frame, bg="#FFE461", borderwidth=2, relief="solid")
                order_frame.pack(fill=tk.X, pady=5)
                tk.Label(order_frame, text=f"Order {order_index + 1}", font=("Cooper Black", 12), bg="#FFE461").pack(pady=5)
                for item in order:
                    if item['size'] != "" or item['crust'] != "" or item['toppings']:
                        item_text = f"Pizza: Size - {item['size']}, Crust - {item['crust']}, Toppings - {', '.join(item['toppings'])}, Quantity - {item['quantity']}, Price - ${item['price'] * item['quantity']:.2f}"
                    else:
                        item_text = f"Beverage: {item['beverage']} x {item['beverage_quantity']}, Price - ${item['price']:.2f}"
                    tk.Label(order_frame, text=item_text, bg="#FFE461").pack(anchor=tk.W)

        tk.Button(frame, text="Back to Home", command=self.create_home_screen).pack(pady=10, side=tk.BOTTOM)



    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_scrollable_canvas(self):
        canvas = tk.Canvas(self.root, bg="#FFE461")
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#FFE461")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        return canvas, scrollable_frame

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaPalace(root)
    root.mainloop()
