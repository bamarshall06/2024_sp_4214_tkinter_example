# view/panel3.py

import tkinter as tk

def create_panel3(parent):
    """Create and return the panel for Button 3."""
    panel = tk.Frame(parent, bg='lightgreen', bd=2, relief=tk.SUNKEN)

    # Add widgets to the panel
    label = tk.Label(panel, text="This is Panel 3")
    label.pack(padx=10, pady=10)

    # Initially hide the panel
    panel.grid_forget()

    return panel
