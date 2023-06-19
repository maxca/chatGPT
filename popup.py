import tkinter as tk
from tkinter import messagebox

# Create a tkinter window
window = tk.Tk()
window.withdraw()  # Hide the main window

# Show a dialog popup
messagebox.showinfo("Dialog Title", "This is a dialog popup!")

# Run the tkinter event loop
window.mainloop()
