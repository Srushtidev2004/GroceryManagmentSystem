import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

def view_table_data(table_name):
    """Fetch and display data from the specified table."""
    conn = sqlite3.connect('grocery.db')
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        columns = [description[0] for description in cursor.description]  # Get column names

        # Clear existing data from the table view
        for row in table_view.get_children():
            table_view.delete(row)

        # Update table view with new columns
        table_view["columns"] = columns
        for col in columns:
            table_view.heading(col, text=col, anchor=tk.CENTER)
            table_view.column(col, anchor=tk.CENTER, width=100)

        # Insert fetched data into the table view
        for row in data:
            table_view.insert('', 'end', values=row)

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"Database error: {e}")
    finally:
        conn.close()

def open_database_viewer():
    """Open the database viewer window."""
    viewer_window = tk.Tk()
    viewer_window.title("Database Viewer")
    viewer_window.geometry("700x500")
    viewer_window.config(bg="#F8F8F8")

    # Title Label
    title_label = tk.Label(
        viewer_window, text="Database Viewer", 
        font=("Arial", 20, "bold"), bg="#F8F8F8", fg="#333"
    )
    title_label.pack(pady=15)

    # Dropdown to select a table
    table_var = tk.StringVar(value="products")
    table_dropdown = ttk.Combobox(
        viewer_window, textvariable=table_var, font=("Arial", 12), width=20
    )
    table_dropdown['values'] = ("products", "employee")
    table_dropdown.pack(pady=10)

    # Button to load data from the selected table
    load_button = tk.Button(
        viewer_window, text="Load Data", font=("Arial", 12, "bold"), 
        bg="#4CAF50", fg="white", width=12, 
        command=lambda: view_table_data(table_var.get())
    )
    load_button.pack(pady=10)

    # Table view to display data
    global table_view
    table_view = ttk.Treeview(viewer_window, show="headings")
    table_view.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

    # Scrollbar for the table view
    scrollbar = ttk.Scrollbar(viewer_window, orient=tk.VERTICAL, command=table_view.yview)
    table_view.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    viewer_window.mainloop()

if __name__ == "__main__":
    open_database_viewer()
