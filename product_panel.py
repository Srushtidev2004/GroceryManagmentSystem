import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def open_product_panel():
    """Open the Product Management Panel."""
    product_window = tk.Tk()
    product_window.title("Product Management Panel")
    product_window.geometry("700x500")
    product_window.config(bg="#F8F8F8")

    # Title Label
    title_label = tk.Label(
        product_window, text="Manage Products", 
        font=("Arial", 20, "bold"), bg="#F8F8F8", fg="#333"
    )
    title_label.pack(pady=20)

    # Product Form Frame
    form_frame = tk.Frame(product_window, bg="#F8F8F8")
    form_frame.pack(pady=10)

    # Product Name Label and Entry
    tk.Label(form_frame, text="Product Name:", font=("Arial", 12), bg="#F8F8F8").grid(row=0, column=0, pady=5, padx=10, sticky="e")
    product_name_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
    product_name_entry.grid(row=0, column=1, pady=5, padx=10)

    # Product Price Label and Entry
    tk.Label(form_frame, text="Product Price:", font=("Arial", 12), bg="#F8F8F8").grid(row=1, column=0, pady=5, padx=10, sticky="e")
    product_price_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
    product_price_entry.grid(row=1, column=1, pady=5, padx=10)

    # Product Quantity Label and Entry
    tk.Label(form_frame, text="Product Quantity:", font=("Arial", 12), bg="#F8F8F8").grid(row=2, column=0, pady=5, padx=10, sticky="e")
    product_quantity_entry = tk.Entry(form_frame, width=30, font=("Arial", 12))
    product_quantity_entry.grid(row=2, column=1, pady=5, padx=10)

    # Buttons Frame
    button_frame = tk.Frame(product_window, bg="#F8F8F8")
    button_frame.pack(pady=10)

    # Add Product Button
    add_product_button = tk.Button(
        button_frame, text="Add Product", font=("Arial", 12), 
        bg="#4CAF50", fg="white", width=12, 
        command=lambda: add_product(product_name_entry.get(), product_price_entry.get(), product_quantity_entry.get())
    )
    add_product_button.grid(row=0, column=0, padx=10)

    # Delete Product Button
    delete_product_button = tk.Button(
        button_frame, text="Delete Product", font=("Arial", 12), 
        bg="#f44336", fg="white", width=12, 
        command=lambda: delete_product(product_name_entry.get())
    )
    delete_product_button.grid(row=0, column=1, padx=10)

    # Product List Frame
    product_list_frame = tk.Frame(product_window, bg="#F8F8F8")
    product_list_frame.pack(pady=10)

    # Product List Label
    product_list_label = tk.Label(
        product_list_frame, text="Product List", 
        font=("Arial", 16, "bold"), bg="#F8F8F8", fg="#333"
    )
    product_list_label.pack(pady=10)

    # Product List Treeview
    global product_treeview
    product_treeview = ttk.Treeview(product_list_frame, columns=("Name", "Price", "Quantity"), show="headings")
    product_treeview.heading("Name", text="Product Name")
    product_treeview.heading("Price", text="Price")
    product_treeview.heading("Quantity", text="Quantity")

    # Scrollbar for the Treeview
    scrollbar = ttk.Scrollbar(product_list_frame, orient=tk.VERTICAL, command=product_treeview.yview)
    product_treeview.configure(yscrollcommand=scrollbar.set)
    product_treeview.pack(fill=tk.BOTH, expand=True, pady=5)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # Load existing products into the Treeview
    load_products()

    product_window.mainloop()

def add_product(name, price, quantity):
    """Add a product to the database."""
    if name and price and quantity:
        try:
            price = float(price)
            quantity = int(quantity)

            conn = sqlite3.connect('grocery.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
            conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")

            load_products()  # Reload product list
        except ValueError:
            messagebox.showerror("Input Error", "Price must be a number and Quantity must be an integer.")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            conn.close()
    else:
        messagebox.showerror("Input Error", "Please fill all fields.")

def delete_product(name):
    """Delete a product from the database."""
    if name:
        conn = sqlite3.connect('grocery.db')
        cursor = conn.cursor()

        cursor.execute("DELETE FROM products WHERE name=?", (name,))
        conn.commit()
        messagebox.showinfo("Success", "Product deleted successfully!")

        load_products()  # Reload product list
        conn.close()
    else:
        messagebox.showerror("Input Error", "Please enter a product name to delete.")

def load_products():
    """Load products from the database into the Treeview."""
    conn = sqlite3.connect('grocery.db')
    cursor = conn.cursor()

    # Clear existing entries in the Treeview
    for row in product_treeview.get_children():
        product_treeview.delete(row)

    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        product_treeview.insert('', 'end', values=row)

    conn.close()

