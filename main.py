import tkinter as tk
from tkinter import font as tkFont
from view.panel1 import create_panel1  # Adjust the import path as needed
from view.panel2 import create_panel2  # Adjust the import path as needed
from view.panel3 import create_panel3  # Adjust the import path as needed

def on_button_click(button_number, panels):
    """Function to handle button click events."""
    # Hide all panels first
    for panel in panels.values():
        panel.grid_forget()

    # Show the selected panel
    if button_number in panels:
        panels[button_number].grid(row=1, column=0, sticky="nsew")
    print(f"Button {button_number} clicked")

def setup_gui(root):
    """Function to set up the GUI components."""
    root.state('zoomed')
    root.columnconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)  # Allow the panel area to expand

    larger_font = tkFont.Font(size=14)

    toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
    toolbar.grid(row=0, column=0, sticky="ew")

    # Create Panels
    panel1 = create_panel1(root)
    panel2 = create_panel2(root)
    panel3 = create_panel3(root)
    panels = {1: panel1, 2: panel2, 3: panel3}  # Dictionary to manage panels

    # Create buttons for the toolbar
    button1 = tk.Button(toolbar, text="Button 1", command=lambda: on_button_click(1, panels), font=larger_font)
    button1.pack(side=tk.LEFT, padx=5, pady=5)

    button2 = tk.Button(toolbar, text="Button 2", command=lambda: on_button_click(2, panels), font=larger_font)
    button2.pack(side=tk.LEFT, padx=5, pady=5)

    button3 = tk.Button(toolbar, text="Button 3", command=lambda: on_button_click(3, panels), font=larger_font)
    button3.pack(side=tk.LEFT, padx=5, pady=5)

def main():
    root = tk.Tk()
    setup_gui(root)
    root.mainloop()

if __name__ == "__main__":
    main()
