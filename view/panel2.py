# view/panel2.py

import tkinter as tk

def create_panel2(parent):
    """Create and return the panel for Button 2."""
    panel = tk.Frame(parent, bg='lightblue', bd=2, relief=tk.SUNKEN)

    # Add widgets to the panel
    label = tk.Label(panel, text="This is Panel 2")
    label.pack(padx=10, pady=10)

    # Initially hide the panel
    panel.grid_forget()

    return panel
