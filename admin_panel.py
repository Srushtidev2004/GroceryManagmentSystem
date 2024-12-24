import tkinter as tk
from tkinter import messagebox
from product_panel import open_product_panel
import sqlite3

def open_admin_panel():
    """Open the Admin Panel."""
    admin_window = tk.Tk()
    admin_window.title("Admin Panel")
    admin_window.geometry("600x500")
    admin_window.config(bg="#F8F8F8")

    # Title Label
    title_label = tk.Label(
        admin_window, text="Admin Control Panel", 
        font=("Arial", 20, "bold"), bg="#F8F8F8", fg="#333"
    )
    title_label.pack(pady=20)

    # Button to manage products
    product_button = tk.Button(
        admin_window, text="Manage Products", font=("Arial", 14), 
        bg="#4CAF50", fg="white", width=18, 
        command=open_product_panel
    )
    product_button.pack(pady=10)

    # Button to manage employees
    manage_employees_button = tk.Button(
        admin_window, text="Manage Employees", font=("Arial", 14), 
        bg="#2196F3", fg="white", width=18, 
        command=open_employee_management
    )
    manage_employees_button.pack(pady=10)

    # Logout Button
    logout_button = tk.Button(
        admin_window, text="Logout", font=("Arial", 14), 
        bg="#f44336", fg="white", width=18, 
        command=admin_window.destroy
    )
    logout_button.pack(pady=10)

    admin_window.mainloop()

def open_employee_management():
    """Open the Employee Management Panel."""
    emp_window = tk.Toplevel()
    emp_window.title("Employee Management")
    emp_window.geometry("600x400")
    emp_window.config(bg="#F8F8F8")

    # Title Label
    title_label = tk.Label(
        emp_window, text="Employee Management", 
        font=("Arial", 20, "bold"), bg="#F8F8F8", fg="#333"
    )
    title_label.pack(pady=20) 

    # Employee Name Label and Entry
    tk.Label(emp_window, text="Employee Username:", font=("Arial", 12), bg="#F8F8F8").pack(pady=5)
    employee_username_entry = tk.Entry(emp_window, width=30, font=("Arial", 12))
    employee_username_entry.pack(pady=5)

    # Employee Password Label and Entry
    tk.Label(emp_window, text="Employee Password:", font=("Arial", 12), bg="#F8F8F8").pack(pady=5)
    employee_password_entry = tk.Entry(emp_window, width=30, font=("Arial", 12), show="*")
    employee_password_entry.pack(pady=5)

    # Add Employee Button
    add_employee_button = tk.Button(
        emp_window, text="Add Employee", font=("Arial", 12), 
        bg="#4CAF50", fg="white", width=18, 
        command=lambda: add_employee(employee_username_entry.get(), employee_password_entry.get())
    )
    add_employee_button.pack(pady=10)

    # Delete Employee Button
    delete_employee_button = tk.Button(
        emp_window, text="Delete Employee", font=("Arial", 12), 
        bg="#f44336", fg="white", width=18, 
        command=lambda: delete_employee(employee_username_entry.get())
    )
    delete_employee_button.pack(pady=10)

def add_employee(username, password):
    """Add a new employee to the database."""
    if username and password:
        conn = sqlite3.connect('grocery.db')
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO employee (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            messagebox.showinfo("Success", "Employee added successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            conn.close()
    else:
        messagebox.showerror("Input Error", "Please fill in all fields.")

def delete_employee(username):
    """Delete an employee from the database."""
    if username:
        conn = sqlite3.connect('grocery.db')
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM employee WHERE username=?", (username,))
            conn.commit()
            messagebox.showinfo("Success", "Employee deleted successfully!")
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"Error: {e}")
        finally:
            conn.close()
    else:
        messagebox.showerror("Input Error", "Please enter a username to delete.")

