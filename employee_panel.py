import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from product_panel import open_product_panel  # Import the product panel function

def employee_login(username, password):
    """Authenticate employee credentials and open the employee panel."""
    conn = sqlite3.connect('grocery.db')
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM employee WHERE username=? AND password=?", (username, password))
        employee = cursor.fetchone()

        if employee:
            open_employee_panel(username)  # Open employee panel if login is successful
        else:
            messagebox.showerror("Login Error", "Invalid employee credentials!")

    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"Error: {e}")
    finally:
        conn.close()

def open_employee_panel(username):
    """Create the Employee Panel."""
    emp_window = tk.Tk()
    emp_window.title(f"Employee Panel - {username}")
    emp_window.geometry("600x400")
    emp_window.config(bg="#F8F8F8")

    # Title Label
    title_label = tk.Label(
        emp_window, text=f"Welcome, {username}", 
        font=("Arial", 20, "bold"), bg="#F8F8F8", fg="#333"
    )
    title_label.pack(pady=20)

    # Button to manage products
    product_button = tk.Button(
        emp_window, text="Manage Products", font=("Arial", 14), 
        bg="#4CAF50", fg="white", width=18, 
        command=open_product_panel
    )
    product_button.pack(pady=10)

    # Logout Button
    logout_button = tk.Button(
        emp_window, text="Logout", font=("Arial", 14), 
        bg="#f44336", fg="white", width=18, 
        command=emp_window.destroy
    )
    logout_button.pack(pady=10)

    emp_window.mainloop()

