import tkinter as tk

def main():
    # create the main window
    root = tk.Tk()
    root.state('zoomed') #make it full sized
    root.title("4214 Inclass Example") #give it a title

    # Add a way to exit the full screen or close the application
    exit_button = tk.Button(root, text="Exit", command=root.destroy)
    exit_button.grid(row=0, column=0, padx=10, pady=10)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()