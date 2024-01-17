# view/panel1.py

import tkinter as tk

def create_panel1(parent):
    """Create and return the panel for Button 1."""
    panel = tk.Frame(parent, bg='lightgray', bd=2, relief=tk.SUNKEN)

    # Add a label to the panel
    label = tk.Label(panel, text="This is Panel 1")
    label.pack(padx=10, pady=10)

    # Create a Listbox with a specified width
    listbox = tk.Listbox(panel, width=20)  # Adjust the width as needed
    listbox.pack(padx=10, pady=10, anchor='nw')  # Pack with north-west anchor

    # Add some sample items to the Listbox
    for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
        listbox.insert(tk.END, item)

    # Initially hide the panel
    panel.grid_forget()

    return panel
