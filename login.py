import tkinter as tk
from tkinter import messagebox
from admin_panel import open_admin_panel
from employee_panel import employee_login

# Hardcoded admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Function to handle login 
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    role = role_var.get()

    if role == "Admin":
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            login_window.destroy()  # Close the login window
            open_admin_panel()
        else:
            messagebox.showerror("Login Error", "Invalid admin credentials!")
    elif role == "Employee":
        employee_login(username, password)

# Create the main login window
login_window = tk.Tk()
login_window.title("Grocery Management System")
login_window.geometry("400x300")
login_window.config(bg="#F0F0F0")

# Title Label
title_label = tk.Label(
    login_window, 
    text="Welcome to Grocery Management", 
    font=("Arial", 18, "bold"), 
    bg="#F0F0F0", 
    fg="#333"
)
title_label.pack(pady=20)

# Login Form Frame
form_frame = tk.Frame(login_window, bg="#F0F0F0")
form_frame.pack(pady=10)

# Username Label and Entry
tk.Label(form_frame, text="Username:", font=("Arial", 12), bg="#F0F0F0").grid(row=0, column=0, pady=5, padx=10, sticky="e")
username_entry = tk.Entry(form_frame, width=25, font=("Arial", 12))
username_entry.grid(row=0, column=1, pady=5, padx=10)

# Password Label and Entry
tk.Label(form_frame, text="Password:", font=("Arial", 12), bg="#F0F0F0").grid(row=1, column=0, pady=5, padx=10, sticky="e")
password_entry = tk.Entry(form_frame, show="*", width=25, font=("Arial", 12))
password_entry.grid(row=1, column=1, pady=5, padx=10)

# Role Selection Frame (Radio Buttons)
role_frame = tk.Frame(login_window, bg="#F0F0F0")
role_frame.pack(pady=10)

role_var = tk.StringVar(value="Admin")
tk.Radiobutton(role_frame, text="Admin", variable=role_var, value="Admin", 
               font=("Arial", 12), bg="#F0F0F0").grid(row=0, column=0, padx=10)
tk.Radiobutton(role_frame, text="Employee", variable=role_var, value="Employee", 
               font=("Arial", 12), bg="#F0F0F0").grid(row=0, column=1, padx=10)

# Login Button
login_button = tk.Button(
    login_window, 
    text="Login", 
    font=("Arial", 12, "bold"), 
    bg="#4CAF50", 
    fg="white", 
    width=10, 
    command=login
)
login_button.pack(pady=15)

# Run the login window
login_window.mainloop()
